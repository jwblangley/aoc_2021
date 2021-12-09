import pytest

from day05 import parse_line_string


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
