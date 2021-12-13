# digit: wires   : length
# 0    : abcefg  : 6
# 1    : cf      : 2
# 2    : acdeg   : 5
# 3    : acdfg   : 5
# 4    : bcdf    : 4
# 5    : abdfg   : 5
# 6    : abdefg  : 6
# 7    : acf     : 3
# 8    : abcdefg : 7
# 9    : abcdfg  : 6

UNIQUE_LENGTHS = [2, 3, 4, 7]


def parse_line(line):
    signal_patterns, output_value = (t.strip().split(" ") for t in line.split("|"))

    return signal_patterns, output_value


def count_match_length_patterns(it, match_lengths=UNIQUE_LENGTHS):
    return len([v for v in it if len(v) in match_lengths])


def determine_mapping(signal_patterns):
    len_signal_mapping = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
    }

    number_mapping = dict()

    for signal in signal_patterns:
        len_signal_mapping[len(signal)].append(signal)

    # 1
    if len(len_signal_mapping[2]) != 1:
        raise ValueError("Unable to determine mapping: 1")
    number_mapping[1] = len_signal_mapping[2][0]

    # 7
    if len(len_signal_mapping[3]) != 1:
        raise ValueError("Unable to determine mapping: 7")
    number_mapping[7] = len_signal_mapping[3][0]

    # 4
    if len(len_signal_mapping[4]) != 1:
        raise ValueError("Unable to determine mapping: 4")
    number_mapping[4] = len_signal_mapping[4][0]

    # 8
    if len(len_signal_mapping[7]) != 1:
        raise ValueError("Unable to determine mapping: 8")
    number_mapping[8] = len_signal_mapping[7][0]

    # 9
    for signal in len_signal_mapping[6]:
        if set(number_mapping[4]).issubset(set(signal)):
            number_mapping[9] = signal
            break
    else:
        raise ValueError("Unable to determine mapping: 9")

    # 0
    for signal in len_signal_mapping[6]:
        if signal not in number_mapping.values() and set(number_mapping[1]).issubset(
            set(signal)
        ):
            number_mapping[0] = signal
            break
    else:
        raise ValueError("Unable to determine mapping: 6")

    # 6
    possible_signals = [
        signal
        for signal in len_signal_mapping[6]
        if signal not in number_mapping.values()
    ]
    if len(possible_signals) != 1:
        raise ValueError("Unable to determine mapping: 0")
    number_mapping[6] = possible_signals[0]

    # 3
    for signal in len_signal_mapping[5]:
        if set(number_mapping[1]).issubset(set(signal)):
            number_mapping[3] = signal
            break
    else:
        raise ValueError("Unable to determine mapping: 9")

    # 5
    for signal in len_signal_mapping[5]:
        if signal not in number_mapping.values() and set(signal).issubset(
            set(number_mapping[6])
        ):
            number_mapping[5] = signal
            break
    else:
        raise ValueError("Unable to determine mapping: 5")

    # 2
    possible_signals = [
        signal
        for signal in len_signal_mapping[5]
        if signal not in number_mapping.values()
    ]
    if len(possible_signals) != 1:
        raise ValueError("Unable to determine mapping: 2")
    number_mapping[2] = possible_signals[0]

    return {"".join(sorted(v)): k for k, v in number_mapping.items()}


def value_from_mapping(value, mapping):
    acc = 0
    for i, v in enumerate(reversed(value)):
        acc += mapping["".join(sorted(v))] * 10 ** i
    return acc


def value_from_line(signal_patterns, output_value):
    mapping = determine_mapping(signal_patterns)
    value = value_from_mapping(output_value, mapping)
    return value


if __name__ == "__main__":
    with open("inputs/day08_input.txt", "r") as data:
        part1 = sum(
            count_match_length_patterns(output_value)
            for signal_patterns, output_value in (parse_line(line) for line in data)
        )

    print(f"Part 1: {part1}")

    with open("inputs/day08_input.txt", "r") as data:
        part2 = sum(value_from_line(*parse_line(line)) for line in data)

    print(f"Part 2: {part2}")
