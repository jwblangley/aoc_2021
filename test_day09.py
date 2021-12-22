import pytest

import numpy as np

from day09 import get_low_points, n_largest_basin_sizes, num_flows_to


@pytest.mark.parametrize(
    "grid,exp",
    [
        ([[1]], [[True]]),
        ([[1, 2], [2, 2]], [[True, False], [False, False]]),
        ([[1, 2], [2, 1]], [[True, False], [False, True]]),
        (
            [[2, 2, 2], [2, 1, 2], [2, 2, 2]],
            [[False, False, False], [False, True, False], [False, False, False]],
        ),
        # fmt: off
        (
            [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
            [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
            [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
            [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]],

            [[False, True, False, False, False, False, False, False, False, True],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, True, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, True, False, False, False]]
        )
        # fmt:on
    ],
)
def test_get_low_points(grid, exp):
    # GIVEN
    """
    input: grid
    expected result: exp
    """
    grid = np.array(grid, dtype=int)
    exp = np.array(exp, dtype=bool)

    # WHEN
    res = get_low_points(grid)

    # THEN
    assert np.array_equal(res, exp)


@pytest.mark.parametrize(
    "grid,i,j,exp",
    [
        ([[1]], 0, 0, 1),
        ([[1, 2], [2, 2]], 0, 0, 4),
        ([[1, 2], [2, 1]], 1, 1, 3),
        ([[2, 2, 2], [2, 1, 2], [2, 2, 0]], 1, 1, 8),
        ([[2, 2, 2], [2, 1, 2], [2, 2, 9]], 1, 1, 8),
        ([[2, 2, 1]], 0, 2, 3),
        ([[2, 2, 1], [1, 2, 3]], 0, 2, 5),
        # fmt: off
        (
            [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
            [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
            [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
            [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]],
            0, 1, 3
        ),
        (
            [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
            [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
            [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
            [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]],
            0, 9, 9
        ),
        (
            [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
            [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
            [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
            [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]],
            2, 2, 14
        ),
        (
            [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
            [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
            [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
            [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]],
            4, 6, 9
        ),
        # fmt:on
    ],
)
def test_num_flows_to(grid, i, j, exp):
    # GIVEN
    """
    input: grid, i, j
    expected value: exp
    """
    grid = np.array(grid, dtype=int)

    # WHEN
    res = num_flows_to(grid, i, j)

    # THEN
    assert res == exp


@pytest.mark.parametrize(
    "grid,n,exp",
    [
        # fmt: off
        (
            [[2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
            [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
            [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
            [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]],
            3,
            [9, 9, 14]
        ),
        # fmt:on
    ],
)
def test_n_largest_basin_sizes(grid, n, exp):
    # GIVEN
    """
    input: grid, n
    expected value: exp
    """
    grid = np.array(grid, dtype=int)

    # WHEN
    res = n_largest_basin_sizes(grid, n)

    # THEN
    assert sorted(res) == sorted(exp)
