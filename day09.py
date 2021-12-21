import numpy as np


def get_low_points(grid):
    pad = np.pad(grid, 1, constant_values=10)

    yp = np.roll(pad, 1, 0)[1:-1, 1:-1]
    yn = np.roll(pad, -1, 0)[1:-1, 1:-1]
    xp = np.roll(pad, 1, 1)[1:-1, 1:-1]
    xn = np.roll(pad, -1, 1)[1:-1, 1:-1]

    return (grid < yp) & (grid < yn) & (grid < xp) & (grid < xn)


if __name__ == "__main__":
    with open("inputs/day09_input.txt", "r") as data:
        grid = np.array([[int(c) for c in line.strip()] for line in data])

    low_points = get_low_points(grid)
    total_risk = (1 + grid)[low_points].sum()
    print(f"Total risk: {total_risk}")
