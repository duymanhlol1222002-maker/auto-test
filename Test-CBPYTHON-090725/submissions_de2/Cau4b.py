# b)
my_tuple = (1, 2, 3)
try:
    my_tuple[1] = 9
except TypeError as e:
    print("TypeError:", e)
    #print("Hello:", e)