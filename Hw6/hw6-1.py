nums = []
numTup = []

while True:
    s = input()
    
    if s == "q":
        break
    nums.append(int(s))

count = []
seen = set()

for number in nums:
    if number not in seen:
        count.append((number, nums.count(number)))
        seen.add(number)

if len(nums) == 0:
    print(f"There is no number")
else:
    print(nums)
    print(count)
