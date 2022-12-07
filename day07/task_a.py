class BaseFile:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    def __repr__(self):
        number_of_parents = 0
        parent = self.parent
        while parent:
            number_of_parents += 1
            parent = parent.parent
        return f"{'  ' * number_of_parents}{self.name}"


class Directory(BaseFile):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.children = {}
        self._size = None

    def add_child(self, child: BaseFile):
        self.children[child.name] = child

    def get_size(self):
        if self._size is not None:
            return self._size
        self._size = sum(child.get_size() for child in self.children.values())
        return self._size

    def yield_all_subdirectories(self):
        yield self
        for child in self.children.values():
            if isinstance(child, Directory):
                yield from child.yield_all_subdirectories()

    def __repr__(self):
        return f"{super().__repr__()}/"


class File(BaseFile):
    def __init__(self, name, size, parent):
        super().__init__(name, parent)
        self.size = size

    def get_size(self):
        return self.size

    def __repr__(self):
        return f"{super().__repr__()} ({self.size})"


class PeekAheadIter:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self._peeked = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._peeked is not None:
            item = self._peeked
            self._peeked = None
            return item
        try:
            return next(self.iterable)
        except StopIteration:
            raise StopIteration()

    def peek(self):
        if self._peeked is None:
            try:
                self._peeked = next(self.iterable)
            except StopIteration:
                # print(f"peeked: <empty>")
                return ""
        # print(f"peeked: {self._peeked}")
        return self._peeked


def convert_numbers(splitted_string: list[str]) -> list[int | str]:
    return [int(s) if s.isdigit() else s for s in splitted_string]


def parse_input(input_txt: str) -> Directory:
    root = Directory("/")
    current_dir = root
    iter_input = PeekAheadIter(iter(input_txt.splitlines()))
    for line in iter_input:
        if not line:
            continue
        match line.split():
            case ["$", "cd", "/"]:
                current_dir = root
            case ["$", "cd", ".."]:
                if not current_dir.parent:
                    raise ValueError("Cannot go up from root")
                current_dir = current_dir.parent
            case ["$", "cd", name]:
                new_dir = Directory(name, current_dir)
                current_dir.add_child(new_dir)
                current_dir = new_dir
            case ["$", "ls"]:
                while iter_input.peek() and not iter_input.peek().startswith("$"):
                    match convert_numbers(ls_output := next(iter_input).split()):
                        case [int(size), name]:
                            current_dir.add_child(File(name, size, current_dir))
                        case ["dir", name]:
                            new_dir = Directory(name, current_dir)
                            current_dir.add_child(new_dir)
                        case _:
                            raise ValueError(
                                "Invalid input, expected file or directory, got {ls_output}"
                            )
            case _:
                raise ValueError(f"Invalid input, expected cd or ls, got {line}")
    return root


def main(input_txt):
    root = parse_input(input_txt)
    total_size = 0
    for dir in root.yield_all_subdirectories():
        if dir.get_size() <= 100_000:
            # print(f"{dir}: {dir.get_size()}")
            total_size += dir.get_size()
    return total_size
