from pathlib import Path

import pytest

from .task_b import main
from .test_a import INPUT


@pytest.mark.parametrize(
    "input_txt, expect",
    [
        pytest.param("A Y", 4),
        pytest.param("B X", 1),
        pytest.param("C Z", 7),
        pytest.param(INPUT, 12),
    ],
)
def test_main(input_txt, expect):
    assert main(input_txt) == expect
