initnum = 0
number = 0
longest_step = -1

while True:
    n = int(input())
    initnum = n
    if n == 0:
        break
    maxium = n
    step = 0
    print("Sequence: ", end = "")
    print(int(n), end = "")
    while n != 1:
        step += 1
        if(n % 2 == 0):
            n //= 2
        else:
            n *= 3
            n += 1
        print(f",{n}", end = "")
        maxium = max(n, maxium)
    print(f"\nSteps: {step}")
    print(f"Max value: {maxium}")
    if step > longest_step:
        longest_step = step
        number = initnum
print(f"Longest sequence produced by: {number}")
print(f"Maximum steps: {longest_step}")