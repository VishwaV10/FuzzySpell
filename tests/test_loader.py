from fuzzyspell.utils.loader import load_words_from_file


def test_load_words():
    trie = load_words_from_file("data/test_words.txt")
    assert trie.search("apple")
    assert trie.search("banana")
    assert not trie.search("carrot")
