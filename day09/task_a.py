from __future__ import annotations

from typing import Literal, NamedTuple


class Point:
    # __slots__ = ("x", "y")

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def as_tuple(self) -> tuple[int, int]:
        return self.x, self.y

    def is_touching(self, other: Point) -> bool:
        return max(abs(self.x - other.x), abs(self.y - other.y)) <= 1

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other: Point) -> Point:
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other: Point) -> Point:
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int) -> Point:
        return Point(self.x * other, self.y * other)

    def __rmul__(self, other: int) -> Point:
        return self * other

    def __neg__(self) -> Point:
        return Point(-self.x, -self.y)

    def __abs__(self) -> int:
        return abs(self.x) + abs(self.y)

    def __str__(self) -> str:
        return f"({self.x},{self.y})"

    def __repr__(self) -> str:
        return f"Point({self.x},{self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y


def get_delta(direction: Literal["R", "U", "L", "D"]) -> Point:
    if direction == "R":
        return Point(1, 0)
    elif direction == "U":
        return Point(0, 1)
    elif direction == "L":
        return Point(-1, 0)
    elif direction == "D":
        return Point(0, -1)
    else:
        raise ValueError(f"Unknown direction: {direction}")


class State:
    def __init__(self, head=Point(0, 0), tail=Point(0, 0)):
        self.head = head
        self.tail = tail
        self._tail_visited = set([tail.as_tuple()])

    def move(self, direction, distance):
        for _ in range(distance):
            self._move(direction)

    def _move(self, direction):
        # move head
        delta = get_delta(direction)
        self.head += delta

        if self.head.is_touching(self.tail):
            return

        match direction:
            case "R":
                self.tail = self.head + Point(-1, 0)
            case "U":
                self.tail = self.head + Point(0, -1)
            case "L":
                self.tail = self.head + Point(1, 0)
            case "D":
                self.tail = self.head + Point(0, 1)
            case _:
                raise ValueError(f"bad direction {direction}")
        self._tail_visited.add(self.tail.as_tuple())


def get_direction_and_distance(input_txt):
    for line in input_txt.splitlines():
        if not line:
            continue
        yield line[0], int(line[1:])


def main(input_txt):
    state = State()

    for direction, distance in get_direction_and_distance(input_txt):
        state.move(direction, distance)

    # # get min and max x and y of all visited points
    # min_x = min_y = 0
    # max_x = max_y = 0
    # for x, y in state._tail_visited:
    #     min_x = min(min_x, x)
    #     min_y = min(min_y, y)
    #     max_x = max(max_x, x)
    #     max_y = max(max_y, y)

    # print(f"min_x: {min_x}, max_x: {max_x}, min_y: {min_y}, max_y: {max_y}")
    return len(state._tail_visited)
