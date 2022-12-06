from pathlib import Path

import pytest

from .task_a import get_priority, main

INPUT = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


@pytest.mark.parametrize(
    "input_txt, expect",
    [
        pytest.param(INPUT, 157),
    ],
)
def test_main(input_txt, expect):
    assert main(input_txt) == expect


@pytest.mark.parametrize(
    "letter, priority",
    [
        pytest.param("p", 16),
        pytest.param("L", 38),
        pytest.param("P", 42),
        pytest.param("v", 22),
        pytest.param("t", 20),
    ],
)
def test_priorities(letter, priority):
    assert get_priority(letter) == priority
