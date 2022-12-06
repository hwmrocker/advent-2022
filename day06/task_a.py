from boltons.iterutils import windowed_iter


def main(input_txt):
    for index, signal in enumerate(windowed_iter(input_txt, 4)):
        # print(f"{index}: {signal}")
        if len(set(signal)) == 4:
            return index + 4
