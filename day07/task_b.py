from .task_a import parse_input


def main(input_txt):
    root = parse_input(input_txt)
    total_size = 70000000
    space_needed_for_update = 30000000
    free_space = total_size - root.get_size()
    space_needed_to_be_deleted = space_needed_for_update - free_space

    possible_dirs_to_delete = []
    for dir in root.yield_all_subdirectories():
        if dir.get_size() >= space_needed_to_be_deleted:
            # print(f"{dir}: {dir.get_size()}")
            possible_dirs_to_delete.append(dir)
    possible_dirs_to_delete.sort(key=lambda d: d.get_size())

    return possible_dirs_to_delete[0].get_size()
