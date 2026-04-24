paragraph = input()
trimed = paragraph.replace("!", "").replace(",", "").replace(".", "").replace("?", "")
print(trimed)

words = trimed.split()

isSeen = []
words.sort()

for word in words:
    if isSeen.__contains__(word):
        continue
    else:
        isSeen.append(word)
        if words.count(word) > 1:
            print(f"{word}:{words.count(word)}")