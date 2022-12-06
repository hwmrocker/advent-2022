from pathlib import Path

import pytest

from .task_a import main

INPUT = """A Y
B X
C Z
"""


@pytest.mark.parametrize(
    "input_txt, expect",
    [
        pytest.param("A Y", 8),
        pytest.param("B X", 1),
        pytest.param("C Z", 6),
        pytest.param(INPUT, 15),
    ],
)
def test_main(input_txt, expect):
    assert main(input_txt) == expect
