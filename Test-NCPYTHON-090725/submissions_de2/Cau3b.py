# b)
def find_first_str(tpl):
    for x in tpl:
        if isinstance(x, str):
            return x
    return None
print(find_first_str((5, 2.5, "abc", True, "xyz")))
