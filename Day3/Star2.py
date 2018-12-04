inputText = [line.rstrip('\n') for line in open('input.txt')]

rects = []
blanket = [["X" for j in range(1000)] for i in range(1000)]
numList = list(range(1, len(inputText) + 1))

for i in range(len(inputText)):
    rects.append([int(x) for x in (inputText[i][inputText[i].index("@"):].split(":", 1)[0].strip()[2:].split(",")) +
                  (inputText[i][inputText[i].index(":"):][2:]).split("x")])

    for j in range(rects[i][2]):
        for k in range(rects[i][3]):
            blank = blanket[j + rects[i][0]][k + rects[i][1]]
            if blank == "X" and blank != 0:
                blanket[j + rects[i][0]][k + rects[i][1]] = i + 1
            else:
                if numList.__contains__(i + 1):
                    numList.remove(i + 1)
                elif numList.__contains__(blank):
                    numList.remove(blank)
                blanket[j + rects[i][0]][k + rects[i][1]] = 0


for m in numList:
    if sum(x.count(m) for x in blanket) == (rects[m - 1][2] * rects[m - 1][3]):
        print("FINAL: " + str(m))
        break
