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


def parse_line(line):
    signal_patterns, output_value = (t.strip().split(" ") for t in line.split("|"))

    return signal_patterns, output_value
