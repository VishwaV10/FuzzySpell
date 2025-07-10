from fuzzyspell.algorithms.damerau_levenshtein import damerau_levenshtein


def test_damerau_levenshtein():
    assert damerau_levenshtein("", "") == 0  # both empty
    assert damerau_levenshtein("a", "") == 1  # deletion
    assert damerau_levenshtein("", "a") == 1  # insertion
    assert damerau_levenshtein("a", "a") == 0  # same single character
    assert damerau_levenshtein("a", "b") == 1  # substitution

    # Transposition cases
    assert damerau_levenshtein("ca", "ac") == 1  # adjacent swap
    assert damerau_levenshtein("abcd", "abdc") == 1  # swap 'c' and 'd'

    # Multiple edits
    assert damerau_levenshtein("example", "samples") == 3

    # Longer words with transpositions
    # 'r' and 's' swapped with others
    assert damerau_levenshtein("converse", "conserve") == 2

    # Identical strings
    assert damerau_levenshtein("testing", "testing") == 0
