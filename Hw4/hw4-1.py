n = int(input())

def count_factors(n):
    result = 0
    for i in range(n):
        if(n % (i + 1) == 0):
            result += 1
    return result

print(count_factors(n))