s = input()
x = int(input())
y = int(input())
vowels = "aeiouAEIOU"
count = 0
for c in s[x-1:y]:
    if c in vowels:
        count += 1
print(count)
