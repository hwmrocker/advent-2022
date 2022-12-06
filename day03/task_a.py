priorities = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_priority(letter: str) -> int:
    return priorities.find(letter)


def main(input_txt):
    total_messed_up_priorities = 0
    for line in input_txt.splitlines():
        compartment_length = len(line) // 2
        assert compartment_length * 2 == len(line)
        compartment_a, compartment_b = (
            line[:compartment_length],
            line[compartment_length:],
        )

        mixup = set(compartment_a) & set(compartment_b)
        assert len(mixup) == 1

        total_messed_up_priorities += get_priority(list(mixup)[0])
    return total_messed_up_priorities
