while True:
    n = input()
    if n == "q":
        break
    n = int(n)
    if n <= 0:
        print(f"{n} is not a positive integer")
    else:
        while n >= 10:
            temp = 0
            base = 1
            while n > 0:
                temp += (n % 10) * base
                base += 1
                n //= 10
            n = temp
        print(n)