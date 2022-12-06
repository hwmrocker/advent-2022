from pathlib import Path

import pytest

from .task_a import main

INPUT = """
"""


@pytest.mark.parametrize(
    "input_txt, expect",
    [
        # pytest.param(INPUT, 820),
        pytest.param("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        pytest.param("nppdvjthqldpwncqszvftbrmjlhg", 6),
        pytest.param("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        pytest.param("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_main(input_txt, expect):
    assert main(input_txt) == expect
