# b)
def longest_word(s):
    words = s.split()
    return max(words, key=len)
print(longest_word("I am learning Python programming"))