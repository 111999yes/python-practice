def isSorted(numbers):
    for i in range(len(numbers)):
        if i == 0:
            continue
        if numbers[i] < numbers[i - 1]:
            return False
    return True

numList = []
while True:
    num = input()
    if(num == "q"):
        break
    numList.append(int(num))

i = 0
cur = numList[1::]
cur.append(numList[0])
flag = False

while i < len(cur):
    if isSorted(cur):
        print(cur)
        flag = True
        break
    else:
        temp = cur[1::]
        temp.append(cur[0])
        cur = temp
    i += 1
if flag == False:
    print("Impossible")