"""
Soundex converts a word into a 4-character code that roughly represents its pronunciation. If two words sound alike, they’ll share
the same code — even if they’re spelled differently.
"""


def soundex(word: str) -> str:
    word = word.lower()
    soundex_mapping = {
        'b': '1', 'f': '1', 'p': '1', 'v': '1',
        'c': '2', 'g': '2', 'j': '2', 'k': '2', 'q': '2', 's': '2', 'x': '2', 'z': '2',
        'd': '3', 't': '3',
        'l': '4',
        'm': '5', 'n': '5',
        'r': '6'
    }
    first_letter = word[0].upper()

    filtered = []
    prev = ''
    for c in word[1:]:
        if c in soundex_mapping:
            digit = soundex_mapping[c]
            if digit != prev:
                filtered.append(digit)
                prev = digit

    filtered = [char for char in filtered if char != '']

    result = first_letter + ''.join(filtered)
    return result.ljust(4, '0')[:4]
