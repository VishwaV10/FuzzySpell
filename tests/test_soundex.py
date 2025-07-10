from fuzzyspell.phonetics.soundex import soundex

print(soundex("garden"))   # Expected: G635
print(soundex("garben"))   # Same or very close
print(soundex("garbel"))   # Slightly different
print(soundex("phone"))    # P500
print(soundex("fone"))     # F500
print(soundex("tomorrow"))  # T560
