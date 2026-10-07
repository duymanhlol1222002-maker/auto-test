

# a)
def flatten_tuple(tpl):
    return tuple(x for sub in tpl for x in sub)
print(flatten_tuple(((1, 2), (3, 4, 5), (6,))))

