nums=[]

while True:
    x=input()
    if x=='q': 
        break
    nums.append(int(x))

if len(nums) == 0:
    print(f"There is no input number")
else:
    sortedNum = sorted(nums, reverse = True)
    rank = []
    for number in nums:
        rank.append(sortedNum.index(number) + 1)
    print(rank)