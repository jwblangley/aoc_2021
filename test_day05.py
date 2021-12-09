import pytest

from day05 import parse_line_string, Point, Line


@pytest.mark.parametrize(
    "line_str,exp",
    [
        ("1,2 -> 3,4", ((1, 2), (3, 4))),
        ("   1,2 -> 3,4", ((1, 2), (3, 4))),
        ("1,  2 -> 3,4", ((1, 2), (3, 4))),
        ("1,2->3,4", ((1, 2), (3, 4))),
        ("1,2   -> 3,4", ((1, 2), (3, 4))),
        ("1,2 ->    3,4", ((1, 2), (3, 4))),
        ("1,2 -> 3,   4", ((1, 2), (3, 4))),
        ("1 , 2 -> 3 , 4", ((1, 2), (3, 4))),
        ("1234,2341 -> 3412,4123", ((1234, 2341), (3412, 4123))),
    ],
)
def test_parse_line_string_valid(line_str, exp):
    # GIVEN
    """
    input: line_str
    expected output: exp
    """

    # WHEN
    res = parse_line_string(line_str)

    # THEN
    assert res == exp


@pytest.mark.parametrize(
    "line_str",
    [
        "1,2 > 3,4",
        "1,2 - > 3,4",
        "1,a -> 3,4",
        "1,2 -> -3,4",
        "1,2 > 3,4",
        "1,2 --> 3,4",
        "1 2 -> 3 4",
        "1,2, -> 3,4",
    ],
)
def test_parse_line_string_invalid(line_str):
    # GIVEN
    """
    input: line_str
    """

    # THEN
    with pytest.raises(ValueError):
        # WHEN
        parse_line_string(line_str)
