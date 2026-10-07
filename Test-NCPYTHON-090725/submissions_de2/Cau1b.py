# b)
def doixung(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
print(doixung("A man a plan a canal Panama"))
