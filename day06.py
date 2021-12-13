import numpy as np

GESTATION_PERIOD = 7
ADULT_AGE = 2


class LaternfishSimulation:
    def __init__(self, arr):
        self.fish = np.array(arr, dtype=int)

    def num_fish(self):
        return len(self.fish)

    def simulate_day(self):
        pass
