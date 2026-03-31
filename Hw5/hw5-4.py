a = int(input())
b = int(input())

fib = [0, 1]
totalLen = max(a, b)

while fib[-1] <= max(a, b):
    fib.append(fib[-1] + fib[-2])

start, end = min(a, b), max(a, b)
result = []

i = 0
while fib[i] <= end:
    if fib[i] >= start and fib[i] <= end:
        result.append(fib[i])
    i += 1
if a > b:
    result = result[::-1]

if len(result) == 0:
    print(f"No Fibonacci numbers found.")
else:
    print(result)