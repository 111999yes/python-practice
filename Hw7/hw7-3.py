pwd = input()

upperCase = 0
lowerCase = 0
digit = 0
special = 0
isUsed = [0, 0, 0, 0]
length = len(pwd)

for c in pwd:
    if c.isupper():
        upperCase += 1
        isUsed[0] = 1
    elif c.islower():
        lowerCase += 1
        isUsed[1] = 1
    elif c.isdigit():
        digit += 1
        isUsed[2] = 1
    else:
        special += 1
        isUsed[3] = 1
catNum = sum(isUsed)
print(f"Uppercase: {upperCase}")
print(f"Lowercase: {lowerCase}")
print(f"Digits: {digit}")
print(f"Special: {special}")
print(f"Length: {length}")
if catNum >= 4 and length >= 8:
    print(f"Strength: Strong")
elif catNum < 3:
    print(f"Strength: Weak")
else:
    print(f"Strength: Medium")