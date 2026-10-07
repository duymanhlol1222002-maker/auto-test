
# a)
def odd_elements(tpl):
    return tuple(x for x in tpl if x % 2 == 1)
print(odd_elements((2, 3, 5, 8, 9, 12, 13)))

