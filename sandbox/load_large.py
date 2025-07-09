from fuzzyspell.utils.loader import load_words_from_file

trie = load_words_from_file("data/words.txt")

# Try searching some common words
for word in ["garden", "apple", "university", "quantum", "xylophone"]:
    print(f"{word}: {trie.search(word)}")
