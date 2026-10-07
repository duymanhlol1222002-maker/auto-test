# Câu 5a: Đếm số lần xuất hiện của từng ký tự trong chuỗi
s = "hello world"
d = {}
for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
print(d)