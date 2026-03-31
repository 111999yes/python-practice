str1_in = input()
str2_in = input()

result = str1_in + str1_in
a = []
for c in str2_in:
    a.append(c)
rev = a[::-1]
for c in rev:
    result += c
print(result)