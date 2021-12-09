from collections import namedtuple

import re

GRID_SIZE = (1000, 1000)

Point = namedtuple("Point", ["x", "y"])
Line = namedtuple("Line", ["start", "end"])


def parse_line_string(line_str):
    pattern = r"^\s*(\d+)\s*,\s*(\d+)\s*->\s*(\d+)\s*,\s*(\d+)\s*$"
    match = re.findall(pattern, line_str)
    if len(match) != 1:
        raise ValueError("Invalid line format")

    x1, y1, x2, y2 = match[0]

    p1 = Point(int(x1), int(y1))
    p2 = Point(int(x2), int(y2))

    return Line(p1, p2)
