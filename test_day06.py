import pytest

import numpy as np

from day06 import LaternfishSimulation


@pytest.mark.parametrize(
    "arr,exp",
    [
        ([1], 1),
        ([1, 2, 3], 3),
        ([1, 1, 1], 3),
        ([1, 1, 1, 1, 1, 1], 6),
    ],
)
def test_num_fish_equal_initial(arr, exp):
    # GIVEN
    """
    input: arr
    expected value: exp
    """

    # WHEN
    sim = LaternfishSimulation(arr)

    # THEN
    assert sim.num_fish() == exp


@pytest.mark.parametrize(
    "arr,exp",
    [
        ([1], [0]),
        ([1, 1, 1, 1], [0, 0, 0, 0]),
        ([1, 2, 3, 4], [0, 1, 2, 3]),
    ],
)
def test_day_decrements_counter(arr, exp):
    # GIVEN
    """
    input: arr
    expected value: exp
    """
    sim = LaternfishSimulation(arr)

    # WHEN
    sim.simulate_day()

    # THEN
    assert np.array_equal(sim.fish, np.array(exp, dtype=int))


@pytest.mark.parametrize(
    "arr,new_total",
    [
        ([0], 2),
        ([0, 0], 4),
        ([0, 1], 3),
        ([0, 1, 2, 0, 2, 0], 9),
        ([1, 1, 1], 3),
    ],
)
def test_reproduce_on_day_zero(arr, new_total):
    # GIVEN
    """
    input: arr
    expected value: new_total
    """
    sim = LaternfishSimulation(arr)

    # WHEN
    sim.simulate_day()

    # THEN
    assert sim.num_fish() == new_total


@pytest.mark.parametrize(
    "arr,exp",
    [
        ([0], [6, 8]),
        ([0, 0], [6, 6, 8, 8]),
        ([0, 1], [6, 0, 8]),
        ([0, 1, 2, 0, 2, 0], [6, 0, 1, 6, 1, 6, 8, 8, 8]),
    ],
)
def test_reproduction_timers(arr, exp):
    # GIVEN
    """
    input: arr
    expected timers: exp
    """
    sim = LaternfishSimulation(arr)

    # WHEN
    sim.simulate_day()

    # THEN
    assert np.array_equal(sim.fish, np.array(exp, dtype=int))


@pytest.mark.parametrize(
    "arr,day_results",
    [
        (
            [3, 4, 3, 1, 2],
            [
                # fmt: off
                [2, 3, 2, 0, 1],
                [1, 2, 1, 6, 0, 8],
                [0, 1, 0, 5, 6, 7, 8],
                [6, 0, 6, 4, 5, 6, 7, 8, 8],
                [5, 6, 5, 3, 4, 5, 6, 7, 7, 8],
                [4, 5, 4, 2, 3, 4, 5, 6, 6, 7],
                [3, 4, 3, 1, 2, 3, 4, 5, 5, 6],
                [2, 3, 2, 0, 1, 2, 3, 4, 4, 5],
                [1, 2, 1, 6, 0, 1, 2, 3, 3, 4, 8],
                [0, 1, 0, 5, 6, 0, 1, 2, 2, 3, 7, 8],
                [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 7, 8, 8, 8],
                [5, 6, 5, 3, 4, 5, 6, 0, 0, 1, 5, 6, 7, 7, 7, 8, 8],
                [4, 5, 4, 2, 3, 4, 5, 6, 6, 0, 4, 5, 6, 6, 6, 7, 7, 8, 8],
                [3, 4, 3, 1, 2, 3, 4, 5, 5, 6, 3, 4, 5, 5, 5, 6, 6, 7, 7, 8],
                [2, 3, 2, 0, 1, 2, 3, 4, 4, 5, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7],
                [1, 2, 1, 6, 0, 1, 2, 3, 3, 4, 1, 2, 3, 3, 3, 4, 4, 5, 5, 6, 8],
                [0, 1, 0, 5, 6, 0, 1, 2, 2, 3, 0, 1, 2, 2, 2, 3, 3, 4, 4, 5, 7, 8],
                [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8, 8, 8],
                # fmt: on
            ],
        )
    ],
)
def test_multi_day_simulation(arr, day_results):
    # GIVEN
    """
    input: arr
    expected day results: day_results
    """
    sim = LaternfishSimulation(arr)
    num_days = len(day_results)

    # WHEN
    acc_results = []
    for i in range(num_days):
        sim.simulate_day()
        acc_results.append(list(sim.fish))

    # THEN
    assert np.array_equal(np.array(acc_results), np.array(day_results))


@pytest.mark.parametrize("arr,days,exp", [([3, 4, 3, 1, 2], 80, 5934)])
def test_long_simulation_total_fish(arr, days, exp):
    # GIVEN
    """
    input: arr, days
    expected result: exp
    """
    sim = LaternfishSimulation(arr)

    # WHEN
    for i in range(days):
        sim.simulate_day()

    # THEN
    assert sim.num_fish() == exp
