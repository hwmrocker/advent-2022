win_condition_lookup = {
    "rock": {
        "rock": "tie",
        "paper": "lose",
        "scissors": "win",
    },
    "paper": {
        "rock": "win",
        "paper": "tie",
        "scissors": "lose",
    },
    "scissors": {
        "rock": "lose",
        "paper": "win",
        "scissors": "tie",
    },
}


def rock_paper_scissors(opponent, my_input) -> int:
    """
    I get 1 point if my_input is rock, 2 for paper, 3 for scissors.
    I get 6 points if I win, 3 points if I draw, 0 points if I lose.
    """
    points_for_my_input = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
    }[my_input]

    match win_condition_lookup[my_input][opponent]:
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
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
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
