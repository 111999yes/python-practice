level = int(input())

if level <= 0:
    print("There is no pattern.")
else:
    arr = [0, 1]
    total = level * (level + 1) // 2
    for i in range(total - 2):
        arr.append(arr[i] + arr[i + 1])
    idx = 0
    for i in range(level):
        for j in range(i + 1):
            print(arr[idx], end = " ")
            idx += 1 
        print()