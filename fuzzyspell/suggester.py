import heapq
from fuzzyspell.algorithms.levenshtein import levenshtein_distance
from fuzzyspell.structures.trie import Trie


def get_suggestions(word: str, trie: Trie, top_k: int = 5) -> list[str]:
    scores = []

    for candidate in trie.words:
        score = levenshtein_distance(word, candidate)
        scores.append((score, candidate))

    heapq.heapify(scores)
    return [candidate for _, candidate in heapq.nsmallest(top_k, scores)]
