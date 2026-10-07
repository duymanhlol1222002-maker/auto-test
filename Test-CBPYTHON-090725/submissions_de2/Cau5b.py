# b)
prices = {"apple": 20, "banana": 10, "orange": 15}
def find_max_price(d):
    return max(d, key=d.get)
print(find_max_price(prices))