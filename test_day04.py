import pytest

import numpy as np

from day04 import BingoBoard, bingo_board_reader


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
    bb = BingoBoard(size, values)

    # THEN
    assert np.array_equal(bb.board, exp)


@pytest.mark.parametrize(
    "size,values,exp",
    [
        (1, [], np.array([])),
        (1, [1, 2, 3, 4], np.array([[[1]], [[2]], [[3]], [[4]]])),
        (2, [1, 2, 3, 4, 5, 6, 7, 8], np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])),
        (
            3,
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            np.array(
                [
                    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                    [[11, 12, 13], [14, 15, 16], [17, 18, 19]],
                ]
            ),
        ),
    ],
)
def test_bingo_board_reader(size, values, exp):
    # GIVEN
    """
    inputs: size, values
    expected board: exp
    """

    # WHEN
    boards = [b.board for b in bingo_board_reader(iter(values), size)]

    # THEN
    assert np.array_equal(np.array(boards), exp)


@pytest.mark.parametrize(
    "size,values",
    [
        (2, [1, 2, 3, 4, 5, 6, 7]),
        (3, [1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 17, 18, 19]),
    ],
)
def test_bingo_board_reader_invalid(size, values):
    # GIVEN
    """
    inputs: size, values
    """

    # THEN
    with pytest.raises(ValueError):
        # WHEN
        boards = [b.board for b in bingo_board_reader(iter(values), size)]
