n = float(input())
epsilon = float(input())

x = 2
while abs(x ** 3 - n) > epsilon:
    x = ((n - x ** 3) / (3 * (x ** 2))) + x
print(f"{x:.3f}")