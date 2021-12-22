import numpy as np


def get_low_points(grid):
    pad = np.pad(grid, 1, constant_values=10)

    yp = np.roll(pad, 1, 0)[1:-1, 1:-1]
    yn = np.roll(pad, -1, 0)[1:-1, 1:-1]
    xp = np.roll(pad, 1, 1)[1:-1, 1:-1]
    xn = np.roll(pad, -1, 1)[1:-1, 1:-1]

    return (grid < yp) & (grid < yn) & (grid < xp) & (grid < xn)


def num_flows_to(grid, i, j, prev=0, seen=None):
    if seen is None:
        seen = set()

    if i < 0 or i >= grid.shape[0] or j < 0 or j >= grid.shape[1]:
        return 0

    if (i, j) in seen:
        return 0

    if grid[i, j] >= 9:
        return 0

    if grid[i, j] >= prev:
        seen.add((i, j))
        return (
            1
            + num_flows_to(grid, i - 1, j, grid[i, j], seen)
            + num_flows_to(grid, i + 1, j, grid[i, j], seen)
            + num_flows_to(grid, i, j - 1, grid[i, j], seen)
            + num_flows_to(grid, i, j + 1, grid[i, j], seen)
        )

    return 0


def n_largest_basin_sizes(grid, n):
    inds = np.dstack(np.meshgrid(np.arange(grid.shape[1]), np.arange(grid.shape[0])))
    lps = get_low_points(grid)
    lp_ids = inds[lps]

    assert len(lp_ids) >= n
    return sorted([num_flows_to(grid, i, j) for j, i in lp_ids])[-n:]


if __name__ == "__main__":
    with open("inputs/day09_input.txt", "r") as data:
        grid = np.array([[int(c) for c in line.strip()] for line in data])

    low_points = get_low_points(grid)
    total_risk = (1 + grid)[low_points].sum()
    print(f"Total risk: {total_risk}")

    three_largest_basin_size_prod = np.prod(n_largest_basin_sizes(grid, 3))
    print(f"Product of three largest basin sizes: {three_largest_basin_size_prod}")
