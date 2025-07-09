# Levenshtein Algorithm

def levenshtein_distance(a: str, b: str) -> int:
    """Returns the Levenshtein Distance between two strings."""
    return min_distance(a, b)


def min_distance(word1: str, word2: str) -> int:
    len1, len2 = len(word1), len(word2)
    # Create a (len1 + 1) x (len2 + 1) DP table
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # Initialize the base cases
    for i in range(len1 + 1):
        dp[i][0] = i  # Deleting all characters from word1 to match an empty word2
    for j in range(len2 + 1):
        dp[0][j] = j  # Inserting all characters into an empty word1 to match word2

    # Fill the DP table
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],    # Deletion
                                   dp[i][j-1],    # Insertion
                                   dp[i-1][j-1])  # Replacement

    # The result is in dp[len1][len2]
    return dp[len1][len2]
