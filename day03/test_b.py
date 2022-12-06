from pathlib import Path

import pytest

from .task_b import main
from .test_a import INPUT


@pytest.mark.parametrize(
    "input_txt, expect",
    [
        pytest.param(INPUT, 70),
    ],
)
def test_main(input_txt, expect):
    assert main(input_txt) == expect
