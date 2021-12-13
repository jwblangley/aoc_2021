import numpy as np

GESTATION_PERIOD = 7
ADULT_AGE = 2


class LaternfishSimulation:
    def __init__(self, arr):
        self.fish = np.array(arr, dtype=int)

    def num_fish(self):
        return len(self.fish)

    def simulate_day(self):
        self.fish -= 1

        # Reproduce
        num_new_fish = len(self.fish[self.fish < 0])
        self.fish[self.fish < 0] = GESTATION_PERIOD - 1
        self.fish = np.append(
            self.fish, [GESTATION_PERIOD + ADULT_AGE - 1] * num_new_fish
        )
