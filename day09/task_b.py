from typing import cast

from rich.console import Console

from .task_a import Point as _Point
from .task_a import State, get_delta, get_direction_and_distance

console = Console()

log = console.log
print = console.print


class Point(_Point):
    # __slots__ = ("x", "y", "name")
    __match_args__ = ("x", "y")

    def __init__(self, x, y, name: str | None = None):
        super().__init__(x, y)
        self.name = name

    def __str__(
        self,
    ):
        if self.name:
            return self.name
        return super().__str__()


class Link(State):
    def __init__(
        self,
        head: Point | None = None,
        tail: Point | None = None,
        name: str = "Z",
    ):
        if head is None:
            head_ = Point(0, 0, name=f"{name.upper()}")
        else:
            head_ = head
            if head.name is None:
                head.name = name.upper()

        if tail is None:
            tail_ = Point(0, 0, name=f"{name.lower()}")
        else:
            tail_ = tail
            if tail.name is None:
                tail.name = name.lower()
        self.head = head_
        self.tail = tail_
        super().__init__(head_, tail_)
        self.name = name

        # delta = get_delta(direction)

    def _move(self, direction, delta: Point | None = None) -> Point | None:
        # print(f"move Link {self.name!r} {direction} {delta!r}")
        # print(f"  head {self.head!r} tail {self.tail!r}")
        # move head
        if delta is None:
            head_delta = get_delta(direction)
        else:
            head_delta = delta
        self.head += head_delta

        if self.head.is_touching(self.tail):
            # print(f"  head {self.head!r} tail {self.tail!r}")
            return

        match direction, head_delta.as_tuple():
            case _, (1, 0):
                #             case Point(1, 0):
                # case "R":
                tail_delta = -self.tail + self.head + Point(-1, 0)
            case _, (0, 1):
                #             case Point(0, 1):
                # case "U":
                tail_delta = -self.tail + self.head + Point(0, -1)
            case _, (-1, 0):
                #             case Point(-1, 0):
                # case "L":
                tail_delta = -self.tail + self.head + Point(1, 0)
            case _, (0, -1):
                #             case Point(0, -1):
                # case "D":
                tail_delta = -self.tail + self.head + Point(0, 1)
            case _, (1, 1):
                #             case Point(1, 1):
                # case "RU":
                if self.tail.x == self.head.x:
                    tail_delta = -self.tail + self.head + Point(0, -1)
                elif self.tail.y == self.head.y:
                    tail_delta = -self.tail + self.head + Point(-1, 0)
                else:
                    tail_delta = delta
            case _, (-1, 1):
                #             case Point(-1, 1):
                # case "LU":
                if self.tail.x == self.head.x:
                    tail_delta = -self.tail + self.head + Point(0, -1)
                elif self.tail.y == self.head.y:
                    tail_delta = -self.tail + self.head + Point(1, 0)
                else:
                    tail_delta = delta
            case _, (-1, -1):
                #             case Point(-1, -1):
                # case "LD":
                if self.tail.x == self.head.x:
                    tail_delta = -self.tail + self.head + Point(0, 1)
                elif self.tail.y == self.head.y:
                    tail_delta = -self.tail + self.head + Point(1, 0)
                else:
                    tail_delta = delta
            case _, (1, -1):
                #             case Point(1, -1):
                # case "RD":
                if self.tail.x == self.head.x:
                    tail_delta = -self.tail + self.head + Point(0, 1)
                elif self.tail.y == self.head.y:
                    tail_delta = -self.tail + self.head + Point(-1, 0)
                else:
                    tail_delta = delta
            case _:
                raise ValueError(f"bad delta {delta!r}")

        # console.log(f"tail_delta {tail_delta!r}")
        dx, dy = tail_delta.as_tuple()
        if abs(dx) > 1 or abs(dy) > 1:
            raise ValueError(f"bad tail_delta {tail_delta!r}")
        self.tail += tail_delta
        self._tail_visited.add(self.tail.as_tuple())
        assert self.tail.is_touching(self.head)
        # print(f"  head {self.head!r} tail {self.tail!r}")

        return tail_delta


class Chain:
    def __init__(self, length):
        self.length = length
        defaults = {
            0: "H",
            # 1: "1",
            # 2: "2",
            # 3: "3",
            # 4: "4",
            # 5: "5",
            # 6: "6",
            # 7: "7",
            # 8: "8",
            # 9: "9",
            # 10: "J",
        }
        self.links = [Link(name=defaults.get(i, str(i))) for i in range(length - 1)]

        # fix tail name for last link
        self.links[-1].tail.name = str(length - 1)

    def move(self, direction, distance):
        # log(f"Moving {direction} {distance}")
        for _ in range(distance):
            # log(_)
            self._move(direction)
            # self.print()
            # input("press enter to continue...")
            # log()

    def _move(self, direction):
        # console.log(f"moving head {direction} {self.links[0].head!r}")
        delta = None
        for link in self.links:
            # log(f"moving {link.head.name} {direction} {delta}")
            delta = link._move(direction, delta)
            if delta is None:
                break

    def _print(
        self,
        bottom_left=Point(-10, -10),
        top_right=Point(10, 10),
        joiner=" ",
        color=True,
        draw_tail=False,
    ):
        self.framebuffer = {}
        # draw background dots
        for y in range(bottom_left.y, top_right.y):
            for x in range(bottom_left.x, top_right.x):
                self.framebuffer[(x, y)] = "."

        # draw tail positions
        if draw_tail:
            for tail_position in self.links[-1]._tail_visited:
                self.framebuffer[tail_position] = "#"

        # draw start position
        self.framebuffer[(0, 0)] = "s"

        # draw tails (to make sure they are always connected to another head)
        for link in reversed(self.links):
            if color:
                value = f"[red]{link.tail.name}[/]"
            else:
                value = link.tail.name
            self.framebuffer[link.tail.as_tuple()] = value

        # draw heads
        for link in reversed(self.links):
            if color:
                value = f"[green]{link.head.name}[/]"
            else:
                value = link.head.name
            self.framebuffer[link.head.as_tuple()] = value

        # print each line from top to bottom
        for y in range(top_right.y - 1, bottom_left.y - 1, -1):
            line = joiner.join(
                # str(x) for x in range(bottom_left.x, top_right.x + 1)
                self.framebuffer[(x, y)]
                for x in range(bottom_left.x, top_right.x)
            )
            yield line
            # print(f"{line}")

    def print(self):
        print(f"[grey underline]next frame[/] 1")
        for line in self._print():
            print(line)


def main(input_txt):
    chain = Chain(10)
    # chain.print()
    # log()
    for direction, distance in get_direction_and_distance(input_txt):
        chain.move(direction, distance)

    return len(chain.links[-1]._tail_visited)
