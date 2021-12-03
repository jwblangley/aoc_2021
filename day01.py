def get_num_increased(it):
    res = 0
    prev = next(it)

    for curr in it:
        if curr > prev:
            res += 1
        prev = curr

    return res


if __name__ == "__main__":
    with open("day01_input.txt", "r") as data:
        res = get_num_increased(int(line) for line in data)

    print(res)
