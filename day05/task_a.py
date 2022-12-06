import re

numbers = re.compile(r"\d+")


def build_stack(input_txt: str):
    lines = input_txt.splitlines()
    stack = []
    last_line = lines.pop()
    for line in last_line.split():
        stack.append([])

    # iterate over the lines in reverse order
    for line in reversed(lines):
        for index, substack in enumerate(stack):
            try:
                element = line[1 + index * 4]
                if element != " ":
                    substack.append(element)
            except IndexError:
                # continue with the next line
                break

    return stack


def move(stack, amount, src, dst):
    for _ in range(amount):
        stack[dst - 1].append(stack[src - 1].pop())


def main(input_txt, move=move):
    stack_input, move_input = input_txt.split("\n\n")
    stack = build_stack(stack_input)
    for line in move_input.splitlines():
        if not line:
            continue
        # print(line)
        amount, src, dst = map(int, numbers.findall(line))
        move(stack, amount, src, dst)
    return "".join(sub_stack[-1] for sub_stack in stack)
