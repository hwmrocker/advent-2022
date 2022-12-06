from pathlib import Path

import pytest

from .task_b import main

INPUT = """
"""


@pytest.mark.parametrize(
    "input_txt, expect",
    [
        # pytest.param(INPUT, 820),
        pytest.param("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        pytest.param("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        pytest.param("nppdvjthqldpwncqszvftbrmjlhg", 23),
        pytest.param("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        pytest.param("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
def test_main(input_txt, expect):
    assert main(input_txt) == expect
