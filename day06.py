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


if __name__ == "__main__":
    NUM_DAYS = 80
    with open("inputs/day06_input.txt", "r") as data:
        line = next(data)
    init_state = [int(t) for t in line.split(",")]
    sim = LaternfishSimulation(init_state)

    for i in range(NUM_DAYS):
        sim.simulate_day()

    print(f"Number of fish after {NUM_DAYS} days: {sim.num_fish()}")
