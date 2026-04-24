expr = input()
tokens = []
i = 0
while i < len(expr):
    if expr[i] == ' ':
        i += 1
        continue
    elif expr[i].isdigit():
        num = 0
        while i < len(expr) and expr[i].isdigit():
            num *= 10
            num += int(expr[i])
            i += 1
        tokens.append(str(num))
    else:
        tokens.append(expr[i])
        i += 1
print(tokens)

left = tokens.count('(')
right = tokens.count(')')
if left == right:
    print("Balanced")
else:
    print("Unbalanced")
print(f"+: {tokens.count('+')}, -: {tokens.count('-')}, *: {tokens.count('*')}, /: {tokens.count('/')}")