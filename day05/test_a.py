from copy import deepcopy
from pathlib import Path

import pytest

from .task_a import build_stack, main, move

INPUT = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

STACK = [
    ["Z", "N"],
    ["M", "C", "D"],
    ["P"],
]


@pytest.mark.parametrize(
    "input_txt, expect",
    [
        pytest.param(INPUT, "CMZ"),
    ],
)
def test_main(input_txt, expect):
    assert main(input_txt) == expect


def test_build_stack():
    stack = build_stack(INPUT.split("\n\n")[0])
    assert stack == STACK


@pytest.mark.parametrize(
    "stack, amount, src, dst, expected",
    [
        pytest.param(
            [["Z", "N"], ["M", "C", "D"], ["P"]],
            1,
            2,
            1,
            [["Z", "N", "D"], ["M", "C"], ["P"]],
            id="1 from 2 to 1",
        ),
        pytest.param(
            [["Z", "N", "D"], ["M", "C"], ["P"]],
            3,
            1,
            3,
            [[], ["M", "C"], ["P", "D", "N", "Z"]],
            id="3 from 1 to 3",
        ),
        pytest.param(
            [["Z", "N"], ["M", "C", "D"], ["P"]],
            2,
            2,
            1,
            [["Z", "N", "D", "C"], ["M"], ["P"]],
            id="2 from 2 to 1",
        ),
        pytest.param(
            [["Z", "N"], ["M", "C", "D"], ["P"]],
            3,
            2,
            1,
            [["Z", "N", "D", "C", "M"], [], ["P"]],
            id="3 from 2 to 1",
        ),
    ],
)
def test_move(stack, amount, src, dst, expected):
    move(stack, amount, src, dst)
    assert stack == expected
