import pytest

import numpy as np

from day04 import BingoBoard


@pytest.mark.parametrize(
    "size,values,exp",
    [
        (1, [1], np.array([[1]])),
        (2, [1, 2, 3, 4], np.array([[1, 2], [3, 4]])),
        (3, [1, 2, 3, 4, 5, 6, 7, 8, 9], np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])),
    ],
)
def test_BingoBoard_creation(size, values, exp):
    # GIVEN
    """
    inputs: size, values
    expected board: exp
    """

    # WHEN
    bb = BingoBoard(size, iter(values))

    # THEN
    assert np.array_equal(bb.board, exp)
