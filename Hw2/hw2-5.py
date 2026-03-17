N = int(input())

if N <= 0:
    print(f"The input {N} is not positive!")

else:
    ans = 0
    for i in range(N):
        if i % 2 == 0:
            ans += 1 / (2 * i + 1)
        else:
            ans -= 1 / (2 * i + 1)
    print(f"Approximated pi/4: {ans:.8f}")