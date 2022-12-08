from typing import TypedDict


def build_board(input_txt):
    board = []
    for line in input_txt.splitlines():
        if line:
            board.append([int(x) for x in line])
    return board


class SearchConfig(TypedDict):
    delta: tuple[int, int]
    start_positions: list[tuple[int, int]]


def get_tree_positions(delta, start_position, width, height):
    """Get the coordinates of all trees in the given direction."""
    x, y = start_position
    while 0 <= x < height and 0 <= y < width:
        yield x, y
        x += delta[0]
        y += delta[1]


def get_visible_trees(board, direction) -> set[tuple[int, int]]:
    """Get the coordinates of all visible trees from the given direction."""

    def get_search_config(direction: str, width: int, height: int) -> SearchConfig:
        match direction:
            case "top":
                return SearchConfig(
                    delta=(1, 0), start_positions=list((0, x) for x in range(width))
                )
            case "right":
                return SearchConfig(
                    delta=(0, -1),
                    start_positions=list((y, width - 1) for y in range(height)),
                )
            case "bottom":
                return SearchConfig(
                    delta=(-1, 0),
                    start_positions=list((height - 1, x) for x in range(width)),
                )
            case "left":
                return SearchConfig(
                    delta=(0, 1), start_positions=list((y, 0) for y in range(height))
                )
            case _:
                raise ValueError(f"Invalid direction: {direction}")

    width = len(board[0])
    height = len(board)
    config = get_search_config(direction, width, height)
    visible_trees = set()
    for start_position in config["start_positions"]:
        max_tree_height = -1
        for tree_position in get_tree_positions(
            config["delta"], start_position, width, height
        ):
            tree = board[tree_position[0]][tree_position[1]]
            if tree > max_tree_height:
                visible_trees.add(tree_position)
                max_tree_height = tree
            if tree == 9:
                # no other tree can be higher than this one
                # time to chekc the next start position
                break
    return visible_trees


def get_all_visible_trees(board) -> set[tuple[int, int]]:
    """Get the coordinates of all visible trees from all directions."""
    visible_trees = set()
    for direction in ("top", "right", "bottom", "left"):
        visible_trees.update(get_visible_trees(board, direction))
    return visible_trees


def main(input_txt):
    board = build_board(input_txt)
    visible_trees = get_all_visible_trees(board)
    return len(visible_trees)
