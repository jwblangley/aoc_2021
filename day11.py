import numpy as np


def get_neighbour_overlaps(grid):
    pad = np.pad(grid, 1, constant_values=False)

    result = np.zeros_like(grid, dtype=int)

    result += np.roll(pad, -1, 0)[1:-1, 1:-1]
    result += np.roll(pad, 1, 0)[1:-1, 1:-1]
    result += np.roll(pad, -1, 1)[1:-1, 1:-1]
    result += np.roll(pad, 1, 1)[1:-1, 1:-1]

    result += np.roll(
        np.pad(np.roll(pad, -1, 0)[1:-1, 1:-1], 1, constant_values=False), -1, 1
    )[1:-1, 1:-1]
    result += np.roll(
        np.pad(np.roll(pad, -1, 0)[1:-1, 1:-1], 1, constant_values=False), 1, 1
    )[1:-1, 1:-1]
    result += np.roll(
        np.pad(np.roll(pad, 1, 0)[1:-1, 1:-1], 1, constant_values=False), -1, 1
    )[1:-1, 1:-1]
    result += np.roll(
        np.pad(np.roll(pad, 1, 0)[1:-1, 1:-1], 1, constant_values=False), 1, 1
    )[1:-1, 1:-1]

    return result


def step(grid):
    all_flashes = np.zeros_like(grid, dtype=bool)
    total_flashes = None

    # Increment
    grid += 1

    while len(grid[all_flashes]) != total_flashes:
        total_flashes = len(grid[all_flashes])

        flashes = grid > 9
        all_flashes |= flashes
        flash_increments = get_neighbour_overlaps(flashes)
        grid += flash_increments

        grid[all_flashes] = 0

    return total_flashes
