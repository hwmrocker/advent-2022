from collections import defaultdict
from functools import reduce

from .task_a import build_board, get_tree_positions


def get_delta(direction):
    match direction:
        case "top":
            return (1, 0)
        case "right":
            return (0, -1)
        case "bottom":
            return (-1, 0)
        case "left":
            return (0, 1)
        case _:
            raise ValueError(f"Invalid direction: {direction}")


def get_scenic_score(board, start_position):
    view_distances = []
    width = len(board[0])
    height = len(board)

    def get_tree(position):
        return board[position[0]][position[1]]

    max_height = get_tree(start_position)
    # print(f"max_height: {max_height}")
    distance = 0
    for start_direction in ("top", "right", "bottom", "left"):
        delta = get_delta(start_direction)
        for distance, tree_position in enumerate(
            get_tree_positions(delta, start_position, width, height)
        ):
            if distance == 0:
                continue
            tree = get_tree(tree_position)
            # print(f" {start_direction} {distance} ({tree_position}): {tree}")
            if tree >= max_height:
                # print(f"  tree too big, stopping")
                view_distances.append(distance)
                break
        else:
            view_distances.append(distance)
    scenic_score = reduce(lambda x, y: x * y, view_distances, 1)
    return scenic_score


def main(input_txt):
    board = build_board(input_txt)
    scenic_scores_by_position = defaultdict(int)
    width = len(board[0])
    height = len(board)

    def yield_start_posisitons():
        for x in range(width):
            for y in range(height):
                yield y, x

    for start_position in yield_start_posisitons():
        scenic_score = get_scenic_score(board, start_position)
        scenic_scores_by_position[start_position] = scenic_score

    return max(scenic_scores_by_position.values())
