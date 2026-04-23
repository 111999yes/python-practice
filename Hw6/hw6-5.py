n = int(input())

numbers = []

for i in range(n):
    value = int(input())
    numbers.append(value)

k = int(input())

segment_sizes = []

for i in range(k):
    size = int(input())
    segment_sizes.append(size)

curIdx = 0
segList = []
for sizeOfSeg in segment_sizes:
    sumofSeg = 0
    subList = numbers[curIdx:curIdx + sizeOfSeg:1]
    for num in subList:
        sumofSeg += num
    segList.append(sumofSeg)
    curIdx += sizeOfSeg
print(numbers)
print(segList)
print(max(segList))