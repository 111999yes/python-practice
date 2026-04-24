import random as r

str_in = input()
numbers = str_in.split(",")
n = int(numbers[0])
m = int(numbers[1])
s = int(numbers[2])

r.seed(s)

curNum = 2
matrix1 = []
for i in range(n):
    col = []
    for j in range(m):
        col.append(curNum)
        curNum += 2
    matrix1.append(col)

matrix2 = []
for i in range(m):
    col = []
    for j in range(2):
        randomNUmber = r.randint(0, 1)
        if randomNUmber == 0:
            col.append(4)
        else:
            col.append(9)
    matrix2.append(col)

resultMatrix = []
for i in range(n):
    col = []
    for j in range(2):
        curResult = 0
        for k in range(m):
            curResult += matrix1[i][k] * matrix2[k][j]
        col.append(curResult)
    resultMatrix.append(col)

print(matrix1)
print(matrix2)
print(resultMatrix)
