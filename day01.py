import collections


def prev_curr_iterator(it):
    prev = next(it)
    for curr in it:
        yield prev, curr
        prev = curr


def summing_window_iterator(it, window_size):
    assert window_size > 0, "Invalid window_size"

    deq = collections.deque([], window_size)
    for _ in range(window_size - 1):
        deq.append(next(it))
    for val in it:
        deq.append(val)
        yield sum(deq)


def get_num_increased(it):
    return sum(1 if curr > prev else 0 for prev, curr in prev_curr_iterator(it))


if __name__ == "__main__":
    with open("inputs/day01_input.txt", "r") as data:
        incr = get_num_increased(int(line) for line in data)
    print(f"Number increased: {incr}")

    with open("inputs/day01_input.txt", "r") as data:
        sum_incr = get_num_increased(
            summing_window_iterator((int(line) for line in data), 3)
        )
    print(f"Number increased (3 window): {sum_incr}")
