import string
# import time
# millis = int(round(time.time() * 1000))
inputText = [line.rstrip('\n') for line in open('input.txt')][0]

alpha = string.ascii_letters
pairs, reverse, removed = [], [], []


def react(string):
    newString = string
    prevNewString = string
    while True:
        for i in range(len(pairs)):
            newString = newString.replace(pairs[i], "").replace(reverse[i], "")
        if prevNewString == newString:
            break
        prevNewString = newString
    return newString


for x in range(int(len(alpha) / 2)):
    pairs.append(alpha[x] + alpha[x + 26])
    reverse.append(alpha[x + 26] + alpha[x])

for y in range(len(pairs)):
    removed.append(react(inputText.replace(pairs[y][0], "").replace(pairs[y][1], "")))

answer = len(min(removed, key=len))
print(answer)
# print(int(round(time.time() * 1000)) - millis)