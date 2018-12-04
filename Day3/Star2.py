import time
millis = int(round(time.time() * 1000))

inputText = [line.rstrip('\n') for line in open('input.txt')]

leftTop = []
widthHeight = []
rects = []
blanket = [["X" for j in range(1000)] for i in range(1000)]

for i in range(len(inputText)):
    leftTop.append(inputText[i][inputText[i].index("@"):].split(":", 1)[0].strip()[2:])
    leftTop[i] = leftTop[i].split(",")
    widthHeight.append((inputText[i][inputText[i].index(":"):][2:]))
    widthHeight[i] = widthHeight[i].split("x")

    rects.append([int(leftTop[i][0]), int(leftTop[i][1]), int(widthHeight[i][0]), int(widthHeight[i][1])])

    for j in range(rects[i][2]):
        for k in range(rects[i][3]):
            blank = blanket[j + rects[i][0]][k + rects[i][1]]
            if blank == "X" and blank != 0:
                blanket[j + rects[i][0]][k + rects[i][1]] = i + 1
            else:
                blanket[j + rects[i][0]][k + rects[i][1]] = 0

oneD = sum(blanket, [])

for m in range(1, len(inputText) + 1):
    if oneD.count(m) == (rects[m - 1][2] * rects[m - 1][3]):
        print("FINAL: " + str(m))
        break

print(int(round(time.time() * 1000)) - millis)
