def main(input_txt):
    calories = []
    for block in input_txt.split("\n\n"):
        calories.append(sum(map(int, block.split())))
    calories.sort()
    return sum(calories[-3:])
