level = int(input())

def draw(n):
    for i in range(n):
        flag = False
        for j in range(n - i - 1):
            print(" ", end = "")
        print("*", end = "")
        for j in range(i):
            count = i - 2 * j
            if(flag == True):
                count = i - 2 * (j + 1)
                count = abs(count)
            elif(count < 0):
                flag = True
                count = i - 2 * (j + 1)
                count = abs(count)
            elif(count == 0):
                flag = True
                count += 2
            print(count, end = "*")
        print()


if(level <= 0):
    print("There is no pattern.")
else:
    draw(level)