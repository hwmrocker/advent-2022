def main(input_txt):
    max_calories = 0
    for block in input_txt.split("\n\n"):
        calories = sum(map(int, block.split()))
        max_calories = max(max_calories, calories)
    return max_calories
