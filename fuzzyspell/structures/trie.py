# Trie Data Structure

# A trie, also known as a prefix tree, is a tree-like data structure that stores a dynamic set of strings, where keys are usually
# strings.

# Properties:
# •	Each node represents a single character.
# •	A path from the root to a leaf represents a word.
# •	Efficient for prefix searches.

# Operations:
# •	Insert: Add a word character by character.
# •	Search: Check if a word is present.
# •	Starts With: Check if there is any word with the given prefix.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        self.root.addWord(word)

    def search(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def starts_with(self, prefix):
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

    def get_words_with_prefix(self, prefix):
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return []
            cur = cur.children[c]

        words = []
        self.dfs(cur, prefix, words)
        return words

    def dfs(self, cur, prefix, words):
        if cur.endOfWord:
            words.append(prefix)
        for char, next_node in cur.children.items():
            self.dfs(next_node, prefix + char, words)
