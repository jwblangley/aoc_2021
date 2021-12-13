import pytest

from day08 import (
    count_match_length_patterns,
    determine_mapping,
    parse_line,
    value_from_line,
    value_from_mapping,
)


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


@pytest.mark.parametrize(
    # fmt: off
    "signal_pattern,exp",
    [
        (
            [ "acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"],
            { "abcdefg": 8, "bcdef": 5, "acdfg": 2, "abcdf": 3, "abd": 7, "abcdef": 9, "bcdefg": 6, "abef": 4, "abcdeg": 0, "ab": 1},
        ),
    ],
    # fmt: on
)
def test_determine_mapping(signal_pattern, exp):
    # GIVEN
    """
    input: signal_pattern
    expected value: exp
    """

    # WHEN
    res = determine_mapping(signal_pattern)

    # THEN
    print(res)
    print(exp)
    assert res == exp


@pytest.mark.parametrize(
    "value,mapping,exp",
    [
        ("a", {"a": 3}, 3),
        ("aa", {"a": 3}, 33),
        ("aaa", {"a": 3}, 333),
        ("abc", {"a": 3, "b": 2, "c": 1}, 321),
    ],
)
def test_value_from_mapping(value, mapping, exp):
    # GIVEN
    """
    input: value, mapping
    expected value: exp
    """

    # WHEN
    res = value_from_mapping(value, mapping)

    # THEN
    assert res == exp


@pytest.mark.parametrize(
    "signal_pattern,output_value,exp",
    [
        # fmt: off
        (
            ["acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"],
            ["cdfeb", "fcadb", "cdfeb", "cdbaf"],
            5353
        ),
        (
            ["be", "cfbegad", "cbdgef", "fgaecd", "cgeb", "fdcge", "agebfd", "fecdb", "fabcd", "edb"],
            ["fdgacbe", "cefdb", "cefbgd", "gcbe"],
            8394
        ),
        (
            ["edbfga", "begcd", "cbg", "gc", "gcadebf", "fbgde", "acbgfd", "abcde", "gfcbed", "gfec"],
            ["fcgedb", "cgb", "dgebacf", "gc"],
            9781
        ),
        (
            ["fgaebd", "cg", "bdaec", "gdafb", "agbcfd", "gdcbef", "bgcad", "gfac", "gcb", "cdgabef"],
            ["cg", "cg", "fdcagb", "cbg"],
            1197
        ),
        (
            ["fbegcd", "cbd", "adcefb", "dageb", "afcb", "bc", "aefdc", "ecdab", "fgdeca", "fcdbega"],
            ["efabcd", "cedba", "gadfec", "cb"],
            9361
        ),
        (
            ["aecbfdg", "fbg", "gf", "bafeg", "dbefa", "fcge", "gcbea", "fcaegb", "dgceab", "fcbdga"],
            ["gecf", "egdcabf", "bgf", "bfgea"],
            4873
        ),
        (
            ["fgeab", "ca", "afcebg", "bdacfeg", "cfaedg", "gcfdb", "baec", "bfadeg", "bafgc", "acf"],
            ["gebdcfa", "ecba", "ca", "fadegcb"],
            8418
        ),
        (
            ["dbcfg", "fgd", "bdegcaf", "fgec", "aegbdf", "ecdfab", "fbedc", "dacgb", "gdcebf", "gf"],
            ["cefg", "dcbef", "fcge", "gbcadfe"],
            4548
        ),
        (
            ["bdfegc", "cbegaf", "gecbf", "dfcage", "bdacg", "ed", "bedf", "ced", "adcbefg", "gebcd"],
            ["ed", "bcgafe", "cdgba", "cbgef"],
            1625
        ),
        (
            ["egadfb", "cdbfeg", "cegd", "fecab", "cgb", "gbdefca", "cg", "fgcdab", "egfdb", "bfceg"],
            ["gbdfcae", "bgc", "cg", "cgb"],
            8717
        ),
        (
            ["gcafb", "gcf", "dcaebfg", "ecagb", "gf", "abcdeg", "gaef", "cafbge", "fdbac", "fegbdc"],
            ["fgae", "cfgab", "fg", "bagce"],
            4315
        ),
        # fmt: on
    ],
)
def test_seven_segment_integration(signal_pattern, output_value, exp):
    # GIVEN
    """
    input: signal_patter, output_value
    expected value: exp
    """

    # WHEN
    res = value_from_line(signal_pattern, output_value)

    # THEN
    assert res == exp
