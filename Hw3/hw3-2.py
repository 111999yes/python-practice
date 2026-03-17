n = int(input())
target = int(input())
sum_limit = int(input())

sum = 0
num = [1, 1]
last_idx = 0
even_term = 0
for i in range(n):
    sum += num[i]
    if num[i] % 2 == 0:
        even_term += 1
    
    print(num[i], end = " ")
    num.append(num[i] + num[i + 1])
    
    if num[i + 1] >= target:
        print(f"\nSum: {sum}")
        print(f"Even terms: {even_term}")
        print(f"Early stop because the term exceeds the target at the {i + 2}-th term")
        break
    elif sum + num[i + 1] >= sum_limit:
        print(f"\nSum: {sum}")
        print(f"Even terms: {even_term}")
        print(f"Early stop because the sum exceeds the limit at the {i + 2}-th term")
        break
    if i == n - 1:
        print(f"\nSum: {sum}")
        print(f"Even terms: {even_term}")
        break
