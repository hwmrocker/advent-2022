import pytest
from pathlib import Path
from .task_b import main

INPUT = """
"""


@pytest.mark.parametrize(
    "input_txt, expect",
    [
        # pytest.param(INPUT, 820),
    ],
)
def test_main(input_txt, expect):
    assert main(input_txt) == expect
