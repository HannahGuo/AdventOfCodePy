import string
inputText = [line.rstrip('\n') for line in open('input.txt')][0]

alpha = string.ascii_letters
pairs, reverse = [], []

for x in range(int(len(alpha) / 2)):
    pairs.append(alpha[x] + alpha[x + 26])
    reverse.append(alpha[x + 26] + alpha[x])

newString = inputText
prevNewString = inputText

while True:
    for i in range(len(pairs)):
        newString = newString.replace(pairs[i], "").replace(reverse[i], "")
    if prevNewString == newString:
        break
    prevNewString = newString

print(len(newString))