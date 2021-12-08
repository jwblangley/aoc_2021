import pytest

import numpy as np

from day03 import gamma_epsilon_from_bin, numpy_bin_to_uint, left_match_filtering


@pytest.mark.parametrize(
    "bin,exp",
    [
        (("10", "10"), (2, 1)),
        (("01", "01"), (1, 2)),
        (("10", "01"), (3, 3)),
        (("011101", "010101", "011001"), (29, 34)),
        (
            (
                "00100",
                "11110",
                "10110",
                "10111",
                "10101",
                "01111",
                "00111",
                "11100",
                "10000",
                "11001",
                "00010",
                "01010",
            ),
            (22, 9),
        ),
    ],
)
def test_gamma_episolon_from_bin(bin, exp):
    # GIVEN
    """
    input: bin
    expected output: exp
    """
    bin = iter(bin)
    exp_gamma, exp_epislon = exp

    # WHEN
    gamma, epsilon = gamma_epsilon_from_bin(bin)

    # THEN
    assert gamma == exp_gamma
    assert epsilon == exp_epislon


@pytest.mark.parametrize(
    "bin",
    [
        ("11", "1"),
        ("11", "11", "1"),
        ("11", "1", "11"),
        ("00", "0", "00"),
    ],
)
def test_gamma_episolon_from_bin_mismatched_lengths(bin):
    # GIVEN
    """
    input: bin
    expected output: exp
    """
    bin = iter(bin)

    # THEN
    with pytest.raises(RuntimeError):
        # WHEN
        gamma_epsilon_from_bin(bin)


@pytest.mark.parametrize(
    "np_bin,exp",
    [
        (np.array([1]), 1),
        (np.array([0]), 0),
        (np.array([1, 0]), 2),
        (np.array([1, 1]), 3),
        (np.array([0, 1]), 1),
        (np.array([0, 0, 0, 0, 1]), 1),
        (np.array([1, 0, 1, 0, 1]), 21),
        (np.array([1, 1, 0, 0, 1]), 25),
    ],
)
def test_numpy_bin_to_uint(np_bin, exp):
    # GIVEN
    """
    input: np_bin
    expected output: exp
    """

    # WHEN
    res = numpy_bin_to_uint(np_bin)

    # THEN
    assert res == exp


@pytest.mark.parametrize(
    "arr,prefix,exp",
    [
        (["abc", "bca", "cab"], "a", "abc"),
        (["abc", "bca", "cab"], "b", "bca"),
        (["abc", "bca", "cab"], "c", "cab"),
        (["abc", "acb", "acc"], "ab", "abc"),
        (["acc", "acb", "abc"], "ab", "abc"),
        (
            ["123456789", "123456689", "123455789", "123446789", "123356789"],
            "1234567",
            "123456789",
        ),
    ],
)
def test_left_match_filtering_valid(arr, prefix, exp):
    # GIVEN
    """
    input: arr, prefix
    expected output: exp
    """

    # WHEN
    res = left_match_filtering(arr, prefix)

    # THEN
    assert res == exp
