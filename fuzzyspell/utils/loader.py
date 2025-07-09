from fuzzyspell.structures.trie import Trie


def load_words_from_file(path: str) -> Trie:
    trie = Trie()
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            word = line.strip().lower()
            if word:
                trie.insert(word)
    return trie
