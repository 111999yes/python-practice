n = int(input())
m = int(input())

matrix = []

for i in range(n):
    col = []
    for j in range(m):
        col.append(int(input()))
    matrix.append(col)

for i in range(n):
    print(matrix[i])
if n != m:
    print(f"This matrix does not have valid diagonals")
else:
    mainSum = 0
    for i in range(n):
        mainSum += matrix[i][i]
    secSum = 0
    for i in range(n):
        secSum += matrix[i][n - 1 - i]
    print(f"Main diagonal sum: {mainSum}")
    print(f"Secondary diagonal sum: {secSum}")