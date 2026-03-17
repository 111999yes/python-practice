N = int(input())

def IsPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

ans = 0
for i in range(2, N):
    if IsPrime(i):
        ans += 1

print(f"There are {ans} prime numbers smaller than {N}")