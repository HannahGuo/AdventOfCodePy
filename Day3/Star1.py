import time
millis = int(round(time.time() * 1000))

inputText = [line.rstrip('\n') for line in open('input.txt')]

leftTop = []
widthHeight = []
rects = []
blanket = [[0 for j in range(1000)] for i in range(1000)]

for i in range(len(inputText)):
    leftTop.append(inputText[i][inputText[i].index("@"):].split(":", 1)[0].strip()[2:].split(","))
    widthHeight.append((inputText[i][inputText[i].index(":"):][2:]).split("x"))

    rects.append([int(leftTop[i][0]), int(leftTop[i][1]), int(widthHeight[i][0]), int(widthHeight[i][1])])

    for j in range(rects[i][2]):
        for k in range(rects[i][3]):
            if blanket[j + rects[i][0]][k + rects[i][1]] <= 2:
                blanket[j + rects[i][0]][k + rects[i][1]] += 1



totalNum = len(list(filter((1).__ne__, list(filter((0).__ne__, sum(blanket, []))))))
print(totalNum)
print(int(round(time.time() * 1000)) - millis)
