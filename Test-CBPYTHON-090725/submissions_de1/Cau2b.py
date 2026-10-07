# Câu 2b: Đếm số chữ số trong chuỗi con từ vị trí start đến end
s = input()
start = int(input())
end = int(input())
count = 0
for ch in s[start - 1:end]:
    if ch.isdigit():
        count += 1
print(count)
