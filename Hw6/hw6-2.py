original_list = []

while True:
    s = input()

    if s == 'q' or s == 'Q':
        break

    original_list.append(s)

if len(original_list) == 0:
    print(f"There is no input string")
else:
    print(original_list)
    for i in range(len(original_list)):
        if original_list[i].strip().isalpha():
            original_list[i] = original_list[i].strip().upper()
    print(original_list)