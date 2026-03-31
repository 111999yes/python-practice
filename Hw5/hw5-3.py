a = int(input())
b = int(input())

fib = [0, 1]
totalLen = max(a, b)

while len(fib) <= totalLen:
    fib.append(fib[-1] + fib[-2])

start, end = min(a, b), max(a, b)
result = fib[start:(end + 1)]

if a > b:
    result = result[::-1]
print(result)