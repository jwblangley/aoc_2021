import pytest

from day07 import min_distance_fuel_cost, triangular_number


@pytest.mark.parametrize("arr, exp", [([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 37)])
def test_min_distance_fuel_cost(arr, exp):
    # GIVEN
    """
    input: arr
    expected value: exp
    """

    # WHEN
    res = min_distance_fuel_cost(arr)

    # THEN
    assert res == exp


@pytest.mark.parametrize(
    "val,exp",
    [
        (1, 1),
        (2, 3),
        (3, 6),
        (4, 10),
        (5, 15),
        (6, 21),
        (7, 28),
        (8, 36),
        (9, 45),
        (10, 55),
        (999, 499500),
    ],
)
def test_triangular_number(val, exp):
    # GIVEN
    """
    input: val
    expected value: exp
    """

    # WHEN
    res = triangular_number(val)

    # THEN
    assert res == exp
