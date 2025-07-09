from fuzzyspell.algorithms.levenshtein import levenshtein_distance


def test_levenshtein_basic():
    assert levenshtein_distance("kitten", "sitting") == 3
    assert levenshtein_distance("flaw", "lawn") == 2
    assert levenshtein_distance("gumbo", "gambol") == 2
    assert levenshtein_distance("example", "example") == 0
