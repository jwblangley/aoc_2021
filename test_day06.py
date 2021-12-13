import pytest

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
