import pytest

from day05 import LineIntersections, parse_line_string, is_diagonal, Point, Line


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
        ",2 -> 3,4",
        "1, -> 3,4",
        "1,2 -> ,4",
        "1,2 -> 3,",
        "1,-2 -> 3,4",
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


@pytest.mark.parametrize(
    "line,exp",
    [
        (Line(Point(1, 1), Point(2, 1)), False),
        (Line(Point(1, 1), Point(5, 1)), False),
        (Line(Point(1, 1), Point(2, 2)), True),
        (Line(Point(2, 2), Point(1, 1)), True),
        (Line(Point(1, 1), Point(1, 5)), False),
        (Line(Point(1, 1), Point(3, 5)), True),
    ],
)
def test_is_diagonal(line, exp):
    # GIVEN
    """
    input: line
    expected value: exp
    """

    # WHEN
    res = is_diagonal(line)

    # THEN
    assert res == exp


@pytest.mark.parametrize(
    "line,grid_size",
    [
        (Line(Point(1, 1), Point(3, 1)), (3, 3)),
        (Line(Point(0, 1), Point(5, 1)), (3, 3)),
        (Line(Point(1, 1), Point(2, 3)), (3, 3)),
        (Line(Point(2, 3), Point(1, 1)), (3, 3)),
        (Line(Point(1, 1), Point(1, 5)), (3, 3)),
        (Line(Point(1, -1), Point(2, 2)), (3, 3)),
    ],
)
def test_count_line_invalid(line, grid_size):
    # GIVEN
    """
    input: line
    """
    li = LineIntersections(grid_size)

    # THEN
    with pytest.raises(IndexError):
        # WHEN
        li.count_line(line)
