from pathlib import Path

import pytest

from .task_b import build_board, get_scenic_score, main
from .test_a import INPUT

board = build_board(INPUT)


@pytest.mark.parametrize(
    "input_txt, expect",
    [
        pytest.param(INPUT, 8),
    ],
)
def test_main(input_txt, expect):
    assert main(input_txt) == expect


@pytest.mark.parametrize(
    "position, expect",
    [
        pytest.param((1, 2), 4),
        pytest.param((3, 2), 8),
    ],
)
def test_scenic_score(position, expect):
    assert get_scenic_score(board, position) == expect
