# Câu 4b: Tuple tính chất bất biến sinh lỗi TypeError
try:
    t = (1, 2, 3)
    t[0] = 10
except TypeError as e:
    print(type(e).__name__)
