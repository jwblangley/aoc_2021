def prev_curr_iterator(it):
    prev = next(it)
    for curr in it:
        yield prev, curr
        prev = curr


def get_num_increased(it):
    return sum(1 if curr > prev else 0 for prev, curr in prev_curr_iterator(it))


if __name__ == "__main__":
    with open("inputs/day01_input.txt", "r") as data:
        res = get_num_increased(int(line) for line in data)

    print(res)
