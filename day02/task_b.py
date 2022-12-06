win_condition_lookup = {
    "rock": {
        "tie": "rock",
        "win": "paper",
        "lose": "scissors",
    },
    "paper": {
        "lose": "rock",
        "tie": "paper",
        "win": "scissors",
    },
    "scissors": {
        "win": "rock",
        "lose": "paper",
        "tie": "scissors",
    },
}


def rock_paper_scissors(opponent, win_condition) -> int:
    """
    I get 1 point if my_input is rock, 2 for paper, 3 for scissors.
    I get 6 points if I win, 3 points if I draw, 0 points if I lose.
    """
    my_form = win_condition_lookup[opponent][win_condition]

    points_for_my_input = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
    }[my_form]

    match win_condition:
        case "win":
            return points_for_my_input + 6
        case "tie":
            return points_for_my_input + 3
        case "lose":
            return points_for_my_input
        case _:
            raise ValueError("Invalid win condition")


opponent_lookup = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}

my_lookup = {
    "X": "lose",
    "Y": "tie",
    "Z": "win",
}


def main(input_txt):
    total_score = 0
    for line in input_txt.split("\n"):
        if not line:
            continue
        opponent, my_input = line.split()
        total_score += rock_paper_scissors(
            opponent_lookup[opponent], my_lookup[my_input]
        )
    return total_score
