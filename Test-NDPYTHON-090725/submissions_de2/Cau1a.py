# a)
# a)
def get_strs(lst):
    return [x for x in lst if isinstance(x, str)]
lst = [100, "apple", 3.14, "banana", 200, None]
print(get_strs(lst))
