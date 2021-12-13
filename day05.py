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

        if is_diagonal(line) and not is_fourty_five_degree(line):
            raise ValueError("Unsupported non-fourty-five-degree diagonal line")

        length = max(abs(line.start.x - line.end.x), abs(line.start.y - line.end.y))
        dx = np.sign(line.end.x - line.start.x)
        dy = np.sign(line.end.y - line.start.y)

        for i in range(length + 1):
            self.grid[line.start.y + i * dy, line.start.x + i * dx] += 1


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

    li = LineIntersections(GRID_SIZE)
    with open("inputs/day05_input.txt", "r") as lines:
        for line in (parse_line_string(l) for l in lines):
            li.count_line(line)

    num_overlaps = (li.grid >= 2).sum()
    print(f"Number of overlaps: {num_overlaps}")
