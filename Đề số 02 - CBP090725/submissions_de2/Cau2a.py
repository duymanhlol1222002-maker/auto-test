# Câu 2a: Tính tổng các số âm từ a đến b
a = int(input())
b = int(input())
tong = sum(x for x in range(min(a, b), max(a, b) + 1) if x < 0)
print(tong)
