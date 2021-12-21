import pytest

import numpy as np

from day09 import get_low_points


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
