import pytest

import numpy as np

from day04 import BingoBoard, BingoGame, bingo_board_reader


@pytest.fixture(name="example_board")
def example_board_fixture():
    return BingoBoard(5, range(25))


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


@pytest.mark.parametrize(
    "call_board,exp",
    [
        (np.array([[True]]), True),
        (np.array([[False]]), False),
        (np.array([[True, True], [True, True]]), True),
        (np.array([[False, False], [True, True]]), True),
        (np.array([[False, False], [False, False]]), False),
        (np.array([[False, False], [True, True]]), True),
        (np.array([[True, False], [True, False]]), True),
        (np.array([[False, True], [False, True]]), True),
        (np.array([[True, False], [False, True]]), False),
        (np.array([[False, True], [True, False]]), False),
    ],
)
def test_board_is_winner(call_board, exp):
    # GIVEN
    """
    input: call_board
    expected output: exp
    """
    size = call_board.shape[0]
    board = BingoBoard(size, range(size * size))
    board.board_called = call_board

    # WHEN
    res = board.is_winner()

    # THEN
    assert res == exp


@pytest.mark.parametrize(
    "number,i,j",
    [
        (0, 0, 0),
        (3, 0, 3),
        (22, 4, 2),
        (18, 3, 3),
        (12, 2, 2),
        (8, 1, 3),
    ],
)
def test_board_call_number(example_board, number, i, j):
    # GIVEN
    """
    example board fixture
    call number: number

    expected location: (i,j)
    """
    expected_call_board = np.zeros_like(example_board.board, dtype=bool)
    expected_call_board[i, j] = True

    # WHEN
    example_board.call_number(number)

    # THEN
    assert np.array_equal(example_board.board_called, expected_call_board)


@pytest.mark.parametrize("num_players", list(range(1, 10)))
@pytest.mark.parametrize("board_size", list(range(1, 10)))
def test_integration_basic_bingo_game_single_winner(num_players, board_size):
    # GIVEN
    game = BingoGame(board_size, iter(range(board_size * board_size * num_players)))

    # WHEN
    winners = game.play(iter(range(board_size)))

    # THEN
    assert len(winners) == 1


@pytest.mark.parametrize("num_players", list(range(1, 10)))
@pytest.mark.parametrize("board_size", list(range(1, 10)))
def test_integration_basic_bingo_game_multi_winners(board_size, num_players):
    # GIVEN
    board_values = list(range(board_size * board_size)) * num_players
    game = BingoGame(board_size, iter(board_values))

    # WHEN
    winners = game.play(iter(range(board_size)))

    # THEN
    assert len(winners) == num_players


@pytest.mark.parametrize("num_players", list(range(1, 10)))
@pytest.mark.parametrize("board_size", list(range(1, 10)))
def test_integration_basic_bingo_game_no_winners(board_size, num_players):
    # GIVEN
    game = BingoGame(board_size, iter(range(board_size * board_size * num_players)))

    # WHEN
    winners = game.play(iter(range(board_size - 1)))

    # THEN
    assert len(winners) == 0
