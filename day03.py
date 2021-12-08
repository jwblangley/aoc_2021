import numpy as np


def numpy_bin_to_uint(np_bin):
    bits = len(np_bin)
    acc = 0

    for i in range(bits):
        power = bits - 1 - i
        acc += np_bin[i] << power

    return acc


def avg_bits(bin):
    totals = None
    count = 0

    for line in bin:
        if totals is None:
            totals = np.array([0] * len(line))

        if len(line) != len(totals):
            raise RuntimeError("Mismatched binary lengths")

        totals += np.array([int(c) for c in line])
        count += 1

    avgs = totals / count
    return avgs


def gamma_epsilon_from_bin(bin):
    avgs = avg_bits(bin)
    gamma = (avgs >= 0.5).astype(int)
    epsilon = (avgs <= 0.5).astype(int)

    gamma = numpy_bin_to_uint(gamma)
    epsilon = numpy_bin_to_uint(epsilon)

    return gamma, epsilon


def left_match_filtering(arr, prefix):
    for i in range(len(prefix)):
        arr = [s for s in arr if s.startswith(prefix[: i + 1])]
        if len(arr) == 1:
            return arr[0]
        if len(arr) == 0:
            raise RuntimeError("No match found")


if __name__ == "__main__":
    with open("inputs/day03_input.txt", "r") as binary:
        lines = [line.strip() for line in binary]

    # Part 1
    gamma, epsilon = gamma_epsilon_from_bin(l for l in lines)
    print(f"gamma: {gamma}")
    print(f"epsilon: {epsilon}")
    print(f"Result: {gamma * epsilon}")
