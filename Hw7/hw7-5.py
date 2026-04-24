min_value = float(input())
max_value = float(input())
nbins = int(input())

seglen = (max_value - min_value) / nbins

result = []
for i in range(nbins):
    resultStr = "("
    resultStr += str(i * seglen + min_value)
    resultStr += ", "
    resultStr += str((i + 1) * seglen + min_value)
    resultStr += ")"
    result.append(resultStr)
print("[", end = "")
for i in range(nbins):
    print(result[i], end = ", ")
print("\b\b]")