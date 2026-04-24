import numpy as np
str_in = input()
trim = str_in.strip("\'")

number = [float(x) for x in trim.split(",")]

arr = np.array(number, dtype = float)

formatedElement = [f"{x:>8.2f}" for x in arr]
outputArr =  "    ".join(formatedElement)

mean = np.mean(arr)
sd = np.std(arr)
print(f"The NumPy array is: [{outputArr}]")
print(f"The mean is: {mean:.2f}")
print(f"The standard deviation is: {sd:.2f}")