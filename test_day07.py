import pytest

from day07 import min_distance_meet_point


@pytest.mark.parametrize("arr, exp", [([16, 1, 2, 0, 4, 2, 7, 1, 2, 14], 2)])
def test_min_distance_meet_point(arr, exp):
    # GIVEN
    """
    input: arr
    expected value: exp
    """

    # WHEN
    res = min_distance_meet_point(arr)

    # THEN
    assert res == exp
