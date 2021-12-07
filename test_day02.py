import pytest

from day02 import Location, parse_instructions


@pytest.mark.parametrize(
    "it,exp",
    [
        (iter(("forward 1", "down 1")), Location(1, 1)),
        (iter(("forward 2", "down 3", "up 2")), Location(2, 1)),
        (
            iter(
                (
                    "down 6",
                    "forward 8",
                    "forward 1",
                    "down 8",
                    "down 7",
                    "forward 8",
                    "down 2",
                    "forward 8",
                    "down 4",
                    "forward 1",
                    "down 1",
                    "up 6",
                )
            ),
            Location(26, 22),
        ),
    ],
)
def test_parse_instructions(it, exp):
    # GIVEN
    """
    input: it
    expected result: exp
    """

    # WHEN
    res = parse_instructions(it)

    # THEN
    assert res == exp
