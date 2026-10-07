# a)
def max_num(lst):
    nums = [x for x in lst if isinstance(x, (int, float))]
    return max(nums)
lst = [100, "apple", 3.14, "banana", 200, None]
print(max_num(lst))


