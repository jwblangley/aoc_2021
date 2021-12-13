import pytest

from day08 import parse_line


@pytest.mark.parametrize(
    "line,exp",
    [
        ("abc bc def | abc de fg", (["abc", "bc", "def"], ["abc", "de", "fg"])),
        ("abc bc def|abc de fg", (["abc", "bc", "def"], ["abc", "de", "fg"])),
        ("abc bc def |abc de fg", (["abc", "bc", "def"], ["abc", "de", "fg"])),
        ("abc bc def | abc de fg", (["abc", "bc", "def"], ["abc", "de", "fg"])),
        (
            "badc bd dbeaf cfdbge dfb cfbdea efbag edcfgab dcafe degfca | eacfd acdfbe cbdegf fcbaedg",
            (
                [
                    "badc",
                    "bd",
                    "dbeaf",
                    "cfdbge",
                    "dfb",
                    "cfbdea",
                    "efbag",
                    "edcfgab",
                    "dcafe",
                    "degfca",
                ],
                ["eacfd", "acdfbe", "cbdegf", "fcbaedg"],
            ),
        ),
    ],
)
def test_parse_line_valid(line, exp):
    # GIVEN
    """
    input: line
    expected value: exp
    """

    # WHEN
    res = parse_line(line)

    # THEN
    assert res == exp
