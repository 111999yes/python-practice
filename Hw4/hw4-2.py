n = int(input())

base = 1
sum = 0
for i in range(n):
    sum += base * (i + 1)
    base *= -1
print(f"Alternating sum: {sum}")