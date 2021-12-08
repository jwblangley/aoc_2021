import numpy as np


class BingoBoard:
    def __init__(self, size, values):
        self.board = np.fromiter(values, int, count=size * size).reshape(size, size)
