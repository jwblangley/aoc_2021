import numpy as np


def numpy_bin_to_uint(np_bin):
    bits = len(np_bin)
    acc = 0

    for i in range(bits):
        power = bits - 1 - i
        acc += np_bin[i] << power

    return acc


def gamma_epsilon_from_bin(bin):
    totals = None
    count = 0

    for line in bin:
        if totals is None:
            totals = np.array([0] * len(line))

        if len(line) != len(totals):
            raise RuntimeError("Mismatched binary lengths")

        temp = np.array([int(c) for c in line])
        totals += temp
        count += 1

    avgs = totals / count
    gamma = (avgs >= 0.5).astype(int)
    epsilon = (avgs <= 0.5).astype(int)

    gamma = numpy_bin_to_uint(gamma)
    epsilon = numpy_bin_to_uint(epsilon)

    return gamma, epsilon


if __name__ == "__main__":
    with open("inputs/day03_input.txt", "r") as binary:
        gamma, epsilon = gamma_epsilon_from_bin(line.strip() for line in binary)

    print(f"gamma: {gamma}")
    print(f"epsilon: {epsilon}")
    print(f"Result: {gamma * epsilon}")
