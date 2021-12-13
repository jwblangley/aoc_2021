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


if __name__ == "__main__":
    with open("inputs/day08_input.txt", "r") as data:
        part1 = sum(
            count_match_length_patterns(output_value)
            for signal_patterns, output_value in (parse_line(line) for line in data)
        )

    print(f"Part 1: {part1}")
