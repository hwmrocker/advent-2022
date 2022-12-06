import re

numbers = re.compile(r"\d+")


def main(input_txt):
    partial_overlaps = 0
    for line in input_txt.splitlines():
        a, b, c, d = map(int, numbers.findall(line))

        if a <= c and b >= c:
            partial_overlaps += 1
        elif a <= d and b >= d:
            partial_overlaps += 1
        elif c <= a and b <= d:
            # this total overlap counts also
            partial_overlaps += 1
        elif a <= c and d <= b:
            # this total overlap counts also
            partial_overlaps += 1
    return partial_overlaps
