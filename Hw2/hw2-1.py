x = float(input())

print(f"Absolute value: {abs(x):.2f}")
if x > 0:
    print("The number is positive")
elif x == 0:
    print("The number is zero")
else:
    print("The number is negative")