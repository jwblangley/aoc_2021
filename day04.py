import numpy as np


class BingoBoard:
    def __init__(self, size, values):
        self.board = np.fromiter(values, int, count=size * size).reshape(size, size)
        self.board_called = np.zeros_like(self.board, dtype=bool)

    def is_winner(self):
        return self.board_called.all(0).any() or self.board_called.all(1).any()

    def call_number(self, number):
        self.board_called[self.board == number] = True


def bingo_board_reader(values, board_size):
    while True:
        buffer = [next(values, None) for i in range(board_size * board_size)]

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
        self.last_call = None

    def call_number(self, number):
        for board in self.boards:
            board.call_number(number)
        self.last_call = number

    def winners(self):
        return [b for b in self.boards if b.is_winner()]

    def play(self, calls):
        for call in calls:
            self.call_number(call)
            winners = self.winners()
            if len(winners) > 0:
                return winners
        return []


if __name__ == "__main__":
    BOARD_SIZE = 5
    with open("inputs/day04_input.txt", "r") as game_data:
        calls = (int(c) for c in next(game_data).split(","))
        board_values = (
            v for values in game_data for v in values.strip().split(" ") if v != ""
        )

        bg = BingoGame(BOARD_SIZE, board_values)

        winners = bg.play(calls)

    assert len(winners) == 1

    winning_board = winners[0]
    score = winning_board.board[~winning_board.board_called].sum() * bg.last_call

    print(f"Winning board score: {score}")
