import random

seed = int(input())
n = int(input())

random.seed(seed)

in_circle = 0

for i in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x * x + y * y <= 1:
        in_circle += 1
print(f"Estimated value of pi: {4 * in_circle / n:.6f}")
