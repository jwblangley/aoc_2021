import pytest

from day01 import get_num_increased


@pytest.mark.parametrize(
    "arr,exp",
    [
        (iter((1, 2, 3)), 2),
        (iter((1, 2, 1)), 1),
        (iter((1, 1, 1)), 0),
        (iter((3, 2, 1)), 0),
        (iter((3, 1, 2)), 1),
        (iter((3, 1, 2, 4, 2, 5, 6, 7, 1, 3, 2, 1, 0, 5, 2)), 7),
        (iter((2, 5, 1, 1, 1, 6, 8, 3, 7, 2, 3, 1, 6, 8, 9)), 8),
    ],
)
def test_get_num_increased(arr, exp):
    # GIVEN
    """
    input: arr
    expected result: exp
    """

    # WHEN
    res = get_num_increased(arr)

    # THEN
    assert res == exp
