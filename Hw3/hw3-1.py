import random

seed = int(input())
roll_target = int(input())
count_target = int(input())

random.seed(seed)

def dice_roll():
    result = random.randint(1, 6)
    return result

count = 0
roll_time = 0
isStart = True

print("Start rolling dice: ", end = "")
while True:
    result = dice_roll()
    roll_time += 1
    if isStart:
        print(result, end = "")
        isStart = False
    else:
        print(f",{result}", end = "")
    if result == roll_target:
        count += 1
    if count == count_target:
        break

print(f"\nNumber of dice rolls: {roll_time}")
