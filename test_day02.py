import pytest

from day02 import Location, parse_instructions


@pytest.mark.parametrize(
    "ins,exp",
    [
        (("forward 1", "down 1"), Location(1, 1)),
        (("forward 2", "down 3", "up 2"), Location(2, 1)),
        (
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
            ),
            Location(26, 22),
        ),
    ],
)
def test_parse_instructions_no_aim(ins, exp):
    # GIVEN
    """
    expected result: exp
    """
    it = iter(ins)

    # WHEN
    res = parse_instructions(it, aim=False)

    # THEN
    assert res == exp


@pytest.mark.parametrize(
    "ins", [("sideways 1", "down 1"), ("forwarrd 2", "down 3", "ups 2")]
)
@pytest.mark.parametrize("aim", [True, False])
def test_parse_instructions_command_invalid(ins, aim):
    # GIVEN
    """
    input: aim
    expected result: exp
    """
    it = iter(ins)

    # THEN
    with pytest.raises(RuntimeError):
        # WHEN
        parse_instructions(it, aim)


@pytest.mark.parametrize(
    "ins", [("forward a", "down 1"), ("forward 2", "down 3", "up !")]
)
@pytest.mark.parametrize("aim", [True, False])
def test_parse_instructions_value_invalid(ins, aim):
    # GIVEN
    """
    input: aim
    expected result: exp
    """
    it = iter(ins)

    # THEN
    with pytest.raises(ValueError):
        # WHEN
        parse_instructions(it, aim)


@pytest.mark.parametrize(
    "ins", [("forward 1 1", "down 1"), ("forward 2", "down 3", "up 1 2")]
)
@pytest.mark.parametrize("aim", [True, False])
def test_parse_instructions_syntax_invalid(ins, aim):
    # GIVEN
    """
    input: aim
    expected result: exp
    """
    it = iter(ins)

    # THEN
    with pytest.raises(ValueError):
        # WHEN
        parse_instructions(it, aim)
