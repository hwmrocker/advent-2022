from pathlib import Path

import pytest

from .task_a import main

INPUT = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


@pytest.mark.parametrize(
    "input_txt, expect",
    [
        pytest.param(INPUT, 2),
    ],
)
def test_main(input_txt, expect):
    assert main(input_txt) == expect
