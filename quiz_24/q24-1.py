sum = 0
idx = 0
while True:
    s = input()
    if(s == "q"):
        break
    elif(s == "c"):
        print(f"The current sum and average are: {sum} and {sum / idx:.2f}")
    elif(s == "r"):
        sum = 0
        idx = 0
        print(f"The sum and count are reset to 0")
    else:
        idx += 1
        sum += int(s)
print(f"The final sum and average are: {sum} and {sum / idx:.2f}")