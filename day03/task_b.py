from boltons.iterutils import chunked_iter

from .task_a import get_priority


def main(input_txt):
    group_priorities = 0
    for group in chunked_iter(input_txt.splitlines(), 3):
        a, b, c = map(set, group)
        badge = list(a & b & c)[0]
        group_priorities += get_priority(badge)

    return group_priorities
