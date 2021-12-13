import pytest

from day08 import count_match_length_patterns, parse_line


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


@pytest.mark.parametrize(
    "it,match_lengths,exp",
    [
        (["abc", "ab", "a"], [], 0),
        (["abc", "ab", "a"], [1], 1),
        (["abc", "ab", "a"], [2], 1),
        (["abc", "ab", "a"], [3], 1),
        (["abc", "ab", "a"], [1, 3], 2),
        (["abc", "abc", "a"], [3], 2),
        (["abc", "abc", "a"], [4], 0),
    ],
)
def test_count_match_length_patterns(it, match_lengths, exp):
    # GIVEN
    """
    input: it, match_lengths
    expected value: exp
    """

    # WHEN
    res = count_match_length_patterns(iter(it), match_lengths)

    # THEN
    assert res == exp
