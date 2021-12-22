import pytest

from day10 import is_corrupt_parenthesis


@pytest.mark.parametrize(
    "value, exp",
    [
        ("a", None),
        (")", ")"),
        ("]", "]"),
        ("}", "}"),
        (">", ">"),
        ("()", None),
        ("[]", None),
        ("{}", None),
        ("<>", None),
        ("<abc>", None),
        ("<abc>a", None),
        ("a<abc>a", None),
        ("a<abc>", None),
        ("{)", ")"),
        ("<]", "]"),
        ("<>]", "]"),
        ("[<>]", None),
        ("[<()>]", None),
        ("[<(>)]", ">"),
        ("{([(<{}[<>[]}>{[]{[(<()>", "}"),
        ("[[<[([]))<([[{}[[()]]]", ")"),
        ("[{[{({}]{}}([{[{{{}}([]", "]"),
        ("[<(<(<(<{}))><([]([]()", ")"),
        ("<{([([[(<>()){}]>(<<{{", ">"),
        ("[<>({}){}[([])<>]]", None),
        ("(((((((((())))))))))", None),
    ],
)
def test_is_corrupt_parenthesis(value, exp):
    # GIVEN
    """
    input: value
    expected result: exp
    """

    # WHEN
    res = is_corrupt_parenthesis(value)

    # THEN
    assert res == exp
