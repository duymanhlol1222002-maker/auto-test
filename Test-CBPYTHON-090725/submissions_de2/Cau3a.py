

lst = [100, "apple", 3.14, "banana", 200, None]
list_num = [x for x in lst if isinstance(x, (int, float))]
print(list_num)
