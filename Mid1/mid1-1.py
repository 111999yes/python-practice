n = int(input())

numbers = []

while n > 0:
    numbers.append(n % 10)
    n //= 10

sum = 0
base = 1
for num in numbers:
    sum += num * base
    base *= -1
print(f"{sum}")