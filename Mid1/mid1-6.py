n = int(input())

numbers = []

while n > 0:
    numbers.append(n % 10)
    n //= 10
rev = numbers[::-1]

length = len(rev)

for i in range(length):
    for j in range(i + 1):
        print(rev[j], end = "")
    print()
for i in range(length - 1):
    for j in range(length - i - 1):
        print(rev[j], end = "")
    print()