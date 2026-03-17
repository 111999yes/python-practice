n = int(input())

def is_perfect(n):
    sum = 0
    idx = 1
    while sum < n:
        sum += idx
        idx += 1
    if sum == n:
        return True
    return False

if is_perfect(n):
    print("Perfect number")
else:
    print("Not a perfect number")