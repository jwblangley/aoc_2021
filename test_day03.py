import pytest

from day03 import gamma_epsilon_from_bin


@pytest.mark.parametrize(
    "bin,exp",
    [
        (("10", "10"), (2, 1)),
        (("01", "01"), (1, 2)),
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
