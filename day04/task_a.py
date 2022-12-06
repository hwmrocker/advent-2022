import re

numbers = re.compile(r"\d+")


def main(input_txt):
    total_overlaps = 0
    for line in input_txt.splitlines():
        a, b, c, d = map(int, numbers.findall(line))
        if a <= c and b >= d:
            total_overlaps += 1
        elif c <= a and d >= b:
            total_overlaps += 1
    return total_overlaps
