# b)
nums = (5, 12, 7, 18, 21, 9, 4)
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True
cnt = sum(1 for x in nums if is_prime(x))
print(cnt)