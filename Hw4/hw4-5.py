n = int(input())

sum = 0

while n != 1 and n != 4:
    sum = 0
    while n > 0:
        digit = n % 10
        n //= 10
        sum += int(digit * digit)
    n = sum
if n == 1:
    print("Happy number")
else:
    print("Not a happy number")