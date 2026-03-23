n = int(input())

def draw(n):
    for i in range(n):
        for j in range(n - i):
            print(" ", end = "")
        if(i == 0):
            print("1")
        elif(i == (n - 1)):
            for j in range(n):
                print((j + 1), end = "")
            for j in range(n - 1):
                print((n - 1 - j), end = "")
        else:
            print("1", end = "")
            for j in range(i * 2 - 1):
                print(" ", end = "")
            print("1")

if n <= 0:
    print("There is no pattern.")
else:
    draw(n)