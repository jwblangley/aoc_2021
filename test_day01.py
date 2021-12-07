import pytest

from day01 import get_num_increased, prev_curr_iterator, summing_window_iterator


@pytest.mark.parametrize(
    "it,exp",
    [
        ((1, 2, 3), ((1, 2), (2, 3))),
        ((1, 2, 3, 4, 5, 6), ((1, 2), (2, 3), (3, 4), (4, 5), (5, 6))),
    ],
)
def test_prev_curr_iterator(it, exp):
    # GIVEN
    """
    input: it
    expected result: exp
    """
    it = iter(it)
    exp = iter(exp)

    # WHEN
    res = prev_curr_iterator(it)

    # THEN
    for val in res:
        assert val == next(exp)

    with pytest.raises(StopIteration):
        next(exp)


@pytest.mark.parametrize(
    "it,exp",
    [
        ((1, 2, 3), 2),
        ((1, 2, 1), 1),
        ((1, 1, 1), 0),
        ((3, 2, 1), 0),
        ((3, 1, 2), 1),
        ((3, 1, 2, 4, 2, 5, 6, 7, 1, 3, 2, 1, 0, 5, 2), 7),
        ((2, 5, 1, 1, 1, 6, 8, 3, 7, 2, 3, 1, 6, 8, 9), 8),
    ],
)
def test_get_num_increased(it, exp):
    # GIVEN
    """
    input: it
    expected result: exp
    """
    it = iter(it)

    # WHEN
    res = get_num_increased(it)

    # THEN
    assert res == exp


@pytest.mark.parametrize(
    "it,exp",
    [
        ((1, 2, 3), (6,)),
        ((1, 2, 3, 4, 5, 6), (6, 9, 12, 15)),
        ((1, 0, -2, 6, -4, 2), (-1, 4, 0, 4)),
    ],
)
def test_summing_window_iterator(it, exp):
    # GIVEN
    """
    input: it
    expected result: exp
    """
    it = iter(it)
    exp = iter(exp)

    # WHEN
    res = summing_window_iterator(it, 3)

    # THEN
    for val in res:
        assert val == next(exp)

    with pytest.raises(StopIteration):
        next(exp)
