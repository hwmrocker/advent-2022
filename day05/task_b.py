from .task_a import main as main_a


def move(stack, amount, src, dst):
    to_move = stack[src - 1][-amount:]
    del stack[src - 1][-amount:]
    stack[dst - 1].extend(to_move)


def main(input_txt):
    return main_a(input_txt, move=move)
