flips_in_str = input()

numOfHead = 0
numOfTail = 0

for c in flips_in_str:
    if c == "H":
        numOfHead += 1
    else:
        numOfTail += 1
print(f"Number of flips: {numOfTail + numOfHead}")
print(f"Number of Heads: {numOfHead}")
print(f"Number of Tails: {numOfTail}")