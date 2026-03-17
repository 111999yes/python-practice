n = int(input())


def displayNumPattern(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end = " ")
        for j in range (i + 1):
            print(int(i - j + 1), end = " ")
        if i < n - 1:
            print("")

if n < 1 or n > 9:
    print(f"The input {n} is invalid")
else:
    displayNumPattern(n)

