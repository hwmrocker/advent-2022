from pathlib import Path

import pytest

from .task_a import Point, State, get_direction_and_distance, main

INPUT = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""


@pytest.mark.parametrize(
    "input_txt, expect",
    [
        pytest.param(INPUT, 13),
    ],
)
def test_main(input_txt, expect):
    assert main(input_txt) == expect


def get_test_param(direction, expected, head=None, tail=None):
    match direction.split():
        case [direction_]:
            distance = 1
        case [direction_, distance_]:
            distance = int(distance_)
        case _:
            raise ValueError(f"bad direction {direction}")
    return pytest.param(
        head or Point(0, 0), tail or Point(0, 0), direction_, distance, expected
    )


@pytest.mark.parametrize(
    "head, tail, direction, distance, expected_tail",
    [
        get_test_param("R", Point(0, 0)),
        get_test_param("U", Point(0, 0)),
        get_test_param("D", Point(0, 0)),
        get_test_param("L", Point(0, 0)),
        # head is touching right
        get_test_param("R", Point(1, 0), head=Point(1, 0)),
        get_test_param("U", Point(0, 0), head=Point(1, 0)),
        get_test_param("D", Point(0, 0), head=Point(1, 0)),
        get_test_param("L", Point(0, 0), head=Point(1, 0)),
        # head is touching up
        get_test_param("R", Point(0, 0), head=Point(0, 1)),
        get_test_param("U", Point(0, 1), head=Point(0, 1)),
        get_test_param("D", Point(0, 0), head=Point(0, 1)),
        get_test_param("L", Point(0, 0), head=Point(0, 1)),
        # head is touching left
        get_test_param("R", Point(0, 0), head=Point(-1, 0)),
        get_test_param("U", Point(0, 0), head=Point(-1, 0)),
        get_test_param("D", Point(0, 0), head=Point(-1, 0)),
        get_test_param("L", Point(-1, 0), head=Point(-1, 0)),
        # head is touching down
        get_test_param("R", Point(0, 0), head=Point(0, -1)),
        get_test_param("U", Point(0, 0), head=Point(0, -1)),
        get_test_param("D", Point(0, -1), head=Point(0, -1)),
        get_test_param("L", Point(0, 0), head=Point(0, -1)),
        # head is touching right and up
        get_test_param("R", Point(1, 1), head=Point(1, 1)),
        get_test_param("U", Point(1, 1), head=Point(1, 1)),
        get_test_param("D", Point(0, 0), head=Point(1, 1)),
        get_test_param("L", Point(0, 0), head=Point(1, 1)),
        # head is touching right and down
        get_test_param("R", Point(1, -1), head=Point(1, -1)),
        get_test_param("D", Point(1, -1), head=Point(1, -1)),
        get_test_param("U", Point(0, 0), head=Point(1, -1)),
        get_test_param("L", Point(0, 0), head=Point(1, -1)),
        # head is touching left and up
        get_test_param("L", Point(-1, 1), head=Point(-1, 1)),
        get_test_param("U", Point(-1, 1), head=Point(-1, 1)),
        get_test_param("D", Point(0, 0), head=Point(-1, 1)),
        get_test_param("R", Point(0, 0), head=Point(-1, 1)),
        # head is touching left and down
        get_test_param("L", Point(-1, -1), head=Point(-1, -1)),
        get_test_param("D", Point(-1, -1), head=Point(-1, -1)),
        get_test_param("U", Point(0, 0), head=Point(-1, -1)),
        get_test_param("R", Point(0, 0), head=Point(-1, -1)),
    ],
)
def test_tail_move(head, tail, direction, distance, expected_tail):
    state = State(head=head, tail=tail)
    state.move(direction, distance)
    assert state.tail == expected_tail


def test_get_direction_and_distance():
    list(get_direction_and_distance(INPUT)) == [
        ("R", 4),
        ("U", 4),
        ("L", 3),
        ("D", 1),
        ("R", 4),
        ("D", 1),
        ("L", 5),
        ("R", 2),
    ]
