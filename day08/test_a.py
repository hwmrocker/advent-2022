from pathlib import Path

import pytest

from .task_a import main

INPUT = """30373
25512
65332
33549
35390
"""


@pytest.mark.parametrize(
    "input_txt, expect",
    [
        pytest.param(INPUT, 21),
    ],
)
def test_main(input_txt, expect):
    assert main(input_txt) == expect
