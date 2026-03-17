year = int(input())
month = int(input())
day = int(input())

isLeap = False

if year % 400 == 0:
    isLeap = True
elif year % 4 == 0 and year % 100 != 0:
    isLeap = True


