from pathlib import Path

import pytest

from .task_b import Chain, Point, get_direction_and_distance, main, print
from .test_a import INPUT as INPUT_A

INPUT = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""


@pytest.mark.parametrize(
    "input_txt, expect",
    [
        pytest.param(INPUT, 36),
    ],
)
def test_main(input_txt, expect):
    assert main(input_txt) == expect


def compare_maps(actual_map, expected_map):
    if actual_map != expected_map:
        print("actual_map:")
        for line in actual_map:
            print(line)
        print("expected_map:")
        for line in expected_map:
            print(line)
    assert actual_map == expected_map


@pytest.mark.parametrize(
    "input_txt, dimensions, test_substeps, expected_maps",
    [
        pytest.param(
            INPUT_A,
            (Point(0, 0), Point(6, 5)),
            True,
            [
                ["......", "......", "......", "......", "H....."],
                ["......", "......", "......", "......", "1H...."],
                ["......", "......", "......", "......", "21H..."],
                ["......", "......", "......", "......", "321H.."],
                ["......", "......", "......", "......", "4321H."],
                ["......", "......", "......", "....H.", "4321.."],
                ["......", "......", "....H.", ".4321.", "5....."],
                ["......", "....H.", "....1.", ".432..", "5....."],
                ["....H.", "....1.", "..432.", ".5....", "6....."],
                ["...H..", "....1.", "..432.", ".5....", "6....."],
                ["..H1..", "...2..", "..43..", ".5....", "6....."],
                [".H1...", "...2..", "..43..", ".5....", "6....."],
                ["..1...", ".H.2..", "..43..", ".5....", "6....."],
                ["..1...", "..H2..", "..43..", ".5....", "6....."],
                ["..1...", "...H..", "..43..", ".5....", "6....."],
                ["......", "...1H.", "..43..", ".5....", "6....."],
                ["......", "...21H", "..43..", ".5....", "6....."],
                ["......", "...21.", "..43.H", ".5....", "6....."],
                ["......", "...21.", "..43H.", ".5....", "6....."],
                ["......", "...21.", "..4H..", ".5....", "6....."],
                ["......", "...2..", "..H1..", ".5....", "6....."],
                ["......", "...2..", ".H13..", ".5....", "6....."],
                ["......", "......", "H123..", ".5....", "6....."],
                ["......", "......", ".H23..", ".5....", "6....."],
                ["......", "......", ".1H3..", ".5....", "6....."],
            ],
            id="test input a",
        ),
        pytest.param(
            INPUT,
            (Point(-11, -5), Point(15, 16)),
            False,
            [
                [
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "...........H..............",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                ],
                [
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "...........54321H.........",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                ],
                [
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "................H.........",
                    "................1.........",
                    "................2.........",
                    "................3.........",
                    "...............54.........",
                    "..............6...........",
                    ".............7............",
                    "............8.............",
                    "...........9..............",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                ],
                [
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "........H1234.............",
                    "............5.............",
                    "............6.............",
                    "............7.............",
                    "............8.............",
                    "............9.............",
                    "..........................",
                    "..........................",
                    "...........s..............",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                ],
                [
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    ".........2345.............",
                    "........1...6.............",
                    "........H...7.............",
                    "............8.............",
                    "............9.............",
                    "..........................",
                    "..........................",
                    "...........s..............",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                ],
                [
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "................987654321H",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "...........s..............",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                ],
                [
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "...........s.........98765",
                    ".........................4",
                    ".........................3",
                    ".........................2",
                    ".........................1",
                    ".........................H",
                ],
                [
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "...........s..............",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "H123456789................",
                ],
                [
                    "H.........................",
                    "1.........................",
                    "2.........................",
                    "3.........................",
                    "4.........................",
                    "5.........................",
                    "6.........................",
                    "7.........................",
                    "8.........................",
                    "9.........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "...........s..............",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                ],
                [
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "..........................",
                    "#.........................",
                    "#.............###.........",
                    "#............#...#........",
                    ".#..........#.....#.......",
                    "..#..........#.....#......",
                    "...#........#.......#.....",
                    "....#......s.........#....",
                    ".....#..............#.....",
                    "......#............#......",
                    ".......#..........#.......",
                    "........#........#........",
                    ".........########.........",
                ],
            ],
            id="bigger test input",
        ),
    ],
)
def test_chain_move(input_txt, dimensions, test_substeps, expected_maps):
    chain = Chain(10)
    maps_iter = iter(expected_maps)

    expected_map = next(maps_iter)
    actual_map = list(chain._print(*dimensions, joiner="", color=False))
    compare_maps(actual_map, expected_map)

    for ln, (direction, distance) in enumerate(get_direction_and_distance(input_txt)):
        if ln == 2:
            print("debug")
        for step in range(distance):
            print(f"ln: {ln}, step: {step}")
            chain._move(direction)
            actual_map = list(chain._print(*dimensions, joiner="", color=False))
            if test_substeps:
                try:
                    expected_map = next(maps_iter)
                except StopIteration:
                    print("actual_map:")
                    for line in actual_map:
                        print(line)
                    raise
                compare_maps(actual_map, expected_map)
        if not test_substeps:
            try:
                expected_map = next(maps_iter)
            except StopIteration:
                print("actual_map:")
                for line in actual_map:
                    print(line)
                raise
            compare_maps(actual_map, expected_map)
