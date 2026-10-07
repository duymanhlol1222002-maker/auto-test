
# b)
s = input()
count = 0
for i in range(len(s)-1):
    if int(s[i]) + int(s[i+1]) == 10:
        count += 1
print(count)
