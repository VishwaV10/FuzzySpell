from fuzzyspell import suggester
from fuzzyspell.utils.loader import load_words_from_file

trie = load_words_from_file("data/words.txt")
suggestions = suggester.get_suggestions("garben", trie, top_k=5)
print(suggestions)
