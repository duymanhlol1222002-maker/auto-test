# b)
lst = [100, "apple", 3.14, "banana", 200, None]


# b)
def total_chars(lst):
    return sum(len(x) for x in lst if isinstance(x, str))
print(total_chars(lst))