fibo = [0, 1]    

def nearest_fibo(number):
    idx = 0
    for fibo_number in fibo:
        if(fibo_number > number):
            return fibo[idx - 1]
        idx += 1
  
def is_fibo(number):
    if number >= fibo[-1]:
        while number >= fibo[-1]:
            fibo.append(fibo[-1] + fibo[-2])
    for fibo_number in fibo:
        if(number == fibo_number):
            return True
        elif(fibo_number > number):
            return False
    return False
    
    
  
def print_fibos(number):
    for fibo_number in fibo:
        if fibo_number < number:
            print(fibo_number, end = ",")
        if fibo_number == number:
            print(fibo_number, end = "")
        elif fibo_number > number:
            return    
  
# Do NOT modify the following
count_fibo = 0
count_not_fibo = 0

while True:
    num_in = input()
    
    if num_in == 'q':
        print(f'Fibonacci numbers count: {count_fibo}')
        print(f'Non-Fibonacci numbers count: {count_not_fibo}')
        print(f'Process terminates.')
        break
    
    num_in = int(num_in)
    if is_fibo(num_in):
        print(f'Fibonacci numbers smaller than or equal to {num_in}: ', end = '', sep = '')
        print_fibos(num_in)
        print()
        count_fibo += 1
    else:
        print(f'Largest Fibonacci number smaller than {num_in}: {nearest_fibo(num_in)}')
        count_not_fibo += 1
