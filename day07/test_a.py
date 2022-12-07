from pathlib import Path

import pytest

from .task_a import Directory, File, main, parse_input

INPUT = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


@pytest.mark.parametrize(
    "input_txt, expect",
    [
        pytest.param(INPUT, 95437),
    ],
)
def test_main(input_txt, expect):
    assert main(input_txt) == expect


def test_parse_input():
    root = parse_input(INPUT)
    list_of_direcories = [
        d.name for d in root.children.values() if isinstance(d, Directory)
    ]
    list_of_direcories.sort()

    list_of_files_and_sizes = [
        (f.name, f.size) for f in root.children.values() if isinstance(f, File)
    ]
    list_of_files_and_sizes.sort()

    assert (list_of_direcories, list_of_files_and_sizes) == (
        ["a", "d"],
        [
            ("b.txt", 14848514),
            ("c.dat", 8504156),
        ],
    )

    assert root.children["a"].children["e"].children["i"].size == 584
    assert root.get_size() == 48381165
