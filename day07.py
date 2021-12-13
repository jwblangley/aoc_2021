def min_distance_fuel_cost(arr, burn_rate=lambda x: x):
    return min(
        sum(burn_rate(abs(x - t)) for x in arr) for t in range(min(arr), max(arr))
    )


def triangular_number(x):
    return x * (x + 1) / 2


if __name__ == "__main__":
    with open("inputs/day07_input.txt") as data:
        line = next(data)

    crabs = [int(v) for v in line.split(",")]

    meet_point = min_distance_fuel_cost(crabs)
    print(f"Meet point (linear burn rate): {meet_point}")

    meet_point = min_distance_fuel_cost(crabs)
    print(f"Meet point (linear burn rate): {meet_point}")
