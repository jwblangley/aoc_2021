from collections import namedtuple

import re

import numpy as np

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


def is_diagonal(line):
    return not (line.start.x == line.end.x or line.start.y == line.end.y)


def is_fourty_five_degree(line):
    return abs(line.start.x - line.end.x) == abs(line.start.y - line.end.y)


class LineIntersections:
    def __init__(self, grid_size):
        self.grid = np.zeros(grid_size, dtype=int)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.grid)

    def count_line(self, line):
        (x1, y1), (x2, y2) = line
        height, width = self.grid.shape
        if (
            x1 < 0
            or x1 >= width
            or y1 < 0
            or y1 >= height
            or x2 < 0
            or x2 >= width
            or y2 < 0
            or y2 >= height
        ):
            raise IndexError(
                f"Line overflows grid. line: {line}, grid: {self.grid.shape}"
            )

        if not is_diagonal(line):
            self.grid[min(y1, y2) : max(y1, y2) + 1, min(x1, x2) : max(x1, x2) + 1] += 1
        else:
            raise NotImplementedError("Not yet implemented")


if __name__ == "__main__":
    GRID_SIZE = (1000, 1000)

    li = LineIntersections(GRID_SIZE)
    with open("inputs/day05_input.txt", "r") as lines:
        for line in (
            parse_line_string(l) for l in lines if not is_diagonal(parse_line_string(l))
        ):
            li.count_line(line)

    num_overlaps = (li.grid >= 2).sum()
    print(f"Number of overlaps (no diagonals): {num_overlaps}")
