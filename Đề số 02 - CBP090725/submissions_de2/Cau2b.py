# Câu 2b: Đếm nguyên âm từ vị trí start đến end (1-indexed)
s = input().strip()
start = int(input())
end = int(input())

sub = s[start - 1 : end]
vowels = "aeiouAEIOU"
count = sum(1 for c in sub if c in vowels)
print(count)
