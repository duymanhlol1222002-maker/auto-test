# Câu 2a: Tính tổng các số chẵn trong khoảng từ a đến b
a = int(input())
b = int(input())
tong = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        tong += i
print(tong)
