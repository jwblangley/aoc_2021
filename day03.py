import numpy as np


def numpy_bin_to_uint(np_bin):
    bits = len(np_bin)
    acc = 0

    for i in range(bits):
        power = bits - 1 - i
        acc += np_bin[i] << power

    return acc


def gamma_epsilon_from_bin(bin):
    gamma, epsilon = most_least_common_bits(bin)

    gamma = numpy_bin_to_uint(gamma)
    epsilon = numpy_bin_to_uint(epsilon)

    return gamma, epsilon


def most_least_common_bits(bin):
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
    most = (avgs >= 0.5).astype(int)
    least = (avgs < 0.5).astype(int)
    return most, least


def _rating_from_bin_list(l_bin, oxygen):
    i = 0
    while len(l_bin) > 1:
        oxygen_bit_rating, co2_bit_rating = most_least_common_bits(iter(l_bin))
        oxygen_bit_rating = "".join(oxygen_bit_rating.astype(str))
        co2_bit_rating = "".join(co2_bit_rating.astype(str))
        l_bin = [
            b
            for b in l_bin
            if b[i] == (oxygen_bit_rating if oxygen else co2_bit_rating)[i]
        ]
        i += 1

    if len(l_bin) != 1:
        raise RuntimeError("No match found")

    return l_bin[0]


def oxygen_co2_rating_from_bin(bin):
    arr = list(bin)

    oxygen_rating = _rating_from_bin_list(list(arr), True)
    co2_rating = _rating_from_bin_list(list(arr), False)

    return int(oxygen_rating, 2), int(co2_rating, 2)


if __name__ == "__main__":
    # Part 1
    with open("inputs/day03_input.txt", "r") as binary:
        gamma, epsilon = gamma_epsilon_from_bin(line.strip() for line in binary)

    print(f"gamma: {gamma}")
    print(f"epsilon: {epsilon}")
    print(f"Result: {gamma * epsilon}")

    # Part 2
    with open("inputs/day03_input.txt", "r") as binary:
        oxygen_rating, co2_rating = oxygen_co2_rating_from_bin(
            line.strip() for line in binary
        )

    print(f"oxygen_rating: {oxygen_rating}")
    print(f"co2_rating: {co2_rating}")
    print(f"Result: {oxygen_rating * co2_rating}")
