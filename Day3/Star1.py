inputText = [line.rstrip('\n') for line in open('input.txt')]

blanket = [[0 for j in range(1000)] for i in range(1000)]

for i in range(len(inputText)):
    rects = [int(x) for x in (inputText[i][inputText[i].index("@"):].split(":", 1)[0].strip()[2:].split(",")) +
             (inputText[i][inputText[i].index(":"):][2:]).split("x")]

    for j in range(rects[2]):
        for k in range(rects[3]):
            if blanket[j + rects[0]][k + rects[1]] < 2:
                blanket[j + rects[0]][k + rects[1]] += 1

print(sum(x.count(2) for x in blanket))