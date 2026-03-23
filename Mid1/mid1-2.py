def is_prime(number):
    # Please write your code here
    i = 2
    while i < number:
        if number % i == 0:
            return False
        i += 1
    return True


def nearest_prime(number):
    # Please write your code here
    while True:
        number -= 1
        if is_prime(number):
            return number

    
def print_prime(number):
    # Please write your code here
    curNumber = 2
    while curNumber <= number:
        if is_prime(curNumber) and curNumber != number:
            print(curNumber, end = ",")
        elif curNumber == number:
            print(number, end = "")
        curNumber += 1

    
######### DON'T EDIT BELOW THIS LINE #########
count_prime = 0
count_not_prime = 0

while True:
    num_in = input()
    
    if num_in == 'q':
        print(f'Prime numbers count: {count_prime}')
        print(f'Non-prime numbers count: {count_not_prime}')
        print(f'Process terminates.')
        break
    
    num_in = int(num_in)
    if is_prime(num_in):
        print(f'Prime numbers smaller than or equal to {num_in}: ', end = '', sep = '')
        print_prime(num_in)
        print()
        count_prime += 1
    else:
        print(f'Largest prime number smaller than {num_in}: {nearest_prime(num_in)}')
        count_not_prime += 1

