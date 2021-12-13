import numpy as np

GESTATION_PERIOD = 7
ADULT_AGE = 2


class LaternfishSimulation:
    def __init__(self, arr):
        self.timer_quantities = [0] * (GESTATION_PERIOD + ADULT_AGE)
        for v in arr:
            self.timer_quantities[v] += 1

    def num_fish(self):
        return sum(self.timer_quantities)

    def simulate_day(self):
        num_reproduce = self.timer_quantities[0]
        self.timer_quantities = self.timer_quantities[1:] + [0]

        self.timer_quantities[GESTATION_PERIOD - 1] += num_reproduce
        self.timer_quantities[GESTATION_PERIOD + ADULT_AGE - 1] += num_reproduce


if __name__ == "__main__":
    NUM_DAYS = 80
    with open("inputs/day06_input.txt", "r") as data:
        line = next(data)
    init_state = [int(t) for t in line.split(",")]
    sim = LaternfishSimulation(init_state)

    for i in range(NUM_DAYS):
        sim.simulate_day()

    print(f"Number of fish after {NUM_DAYS} days: {sim.num_fish()}")

    # Part 2
    PART_2_DAYS = 256
    for i in range(PART_2_DAYS - NUM_DAYS):
        sim.simulate_day()

    print(f"Number of fish after {PART_2_DAYS} days: {sim.num_fish()}")
