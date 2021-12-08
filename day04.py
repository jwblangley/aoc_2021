import numpy as np


class BingoBoard:
    def __init__(self, size, values):
        self.board = np.fromiter(values, int, count=size * size).reshape(size, size)
        self.board_called = np.zeros_like(self.board, dtype=bool)

    def is_winner(self):
        return self.board_called.all(0).any() or self.board_called.all(1).any()


def bingo_board_reader(values, board_size):
    while True:
        buffer = [next(values, None) for i in range(board_size * board_size)]
        print(buffer)

        # Consumption finished
        if all(v == None for v in buffer):
            break
        # Consumption failed
        if any(v == None for v in buffer):
            raise ValueError("Insufficient values to build full board")

        yield BingoBoard(board_size, buffer)


class BingoGame:
    def __init__(self, board_size, values):
        self.boards = list(bingo_board_reader(values, board_size))
