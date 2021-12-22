import pytest

from day10 import is_corrupt_parenthesis


@pytest.mark.parametrize(
    "value, exp",
    [
        ("a", []),
        (")", ")"),
        ("]", "]"),
        ("}", "}"),
        (">", ">"),
        ("()", []),
        ("[]", []),
        ("{}", []),
        ("<>", []),
        ("<abc>", []),
        ("<abc>a", []),
        ("a<abc>a", []),
        ("a<abc>", []),
        ("{)", ")"),
        ("<]", "]"),
        ("<>]", "]"),
        ("[<>]", []),
        ("[<()>]", []),
        ("[<(>)]", ">"),
        ("{([(<{}[<>[]}>{[]{[(<()>", "}"),
        ("[[<[([]))<([[{}[[()]]]", ")"),
        ("[{[{({}]{}}([{[{{{}}([]", "]"),
        ("[<(<(<(<{}))><([]([]()", ")"),
        ("<{([([[(<>()){}]>(<<{{", ">"),
        ("[<>({}){}[([])<>]]", []),
        ("(((((((((())))))))))", []),
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
