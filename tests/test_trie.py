from fuzzyspell.structures.trie import Trie


def test_trie():
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("application")

    assert trie.search("apple") is True
    assert trie.search("app") is True
    assert trie.search("appl") is False

    assert trie.starts_with("app") is True
    assert trie.starts_with("apl") is False

    words = trie.get_words_with_prefix("app")
    assert set(words) == {"app", "apple", "application"}

    words = trie.get_words_with_prefix("ban")
    assert words == []
