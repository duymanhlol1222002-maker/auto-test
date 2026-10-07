# b)
def tuple_stats(tpl):
    s = sum(tpl)
    avg = s / len(tpl)
    return (avg, s)
print(tuple_stats((2.5, 3.5, 7.0, 6.0)))
