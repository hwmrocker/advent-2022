from pathlib import Path

import pytest

from .task_a import main

INPUT = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


@pytest.mark.parametrize(
    "input_txt, expect",
    [
        pytest.param(INPUT, 24000),
    ],
)
def test_main(input_txt, expect):
    assert main(input_txt) == expect
