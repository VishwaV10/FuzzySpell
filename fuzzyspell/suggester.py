import heapq
from fuzzyspell.algorithms.levenshtein import levenshtein_distance
from fuzzyspell.phonetics.soundex import soundex
from fuzzyspell.structures.trie import Trie


def get_suggestions(word: str, trie: Trie, top_k: int = 5) -> list[str]:
    scores = []
    input_soundex = soundex(word)

    for candidate in trie.words:
        distance = levenshtein_distance(word, candidate)
        candidate_soundex = soundex(candidate)

        mismatch_count = sum(1 for i, j in zip(
            input_soundex, candidate_soundex) if i != j)
        penalty = mismatch_count * 0.2

        scores.append((distance + penalty, candidate))

    heapq.heapify(scores)
    return [candidate for _, candidate in heapq.nsmallest(top_k, scores)]
