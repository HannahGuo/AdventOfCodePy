inputText = [line.rstrip('\n') for line in open('input.txt')]

sortedDates = sorted(inputText)

guardOrder = [sortedDates[x].split("#")[1].split(" ", 1)[0] for x in range(len(sortedDates))
              if sortedDates[x].__contains__("#")]

numGuards = list(set(guardOrder))

times = [int(sortedDates[x].split(":")[1].split("]", 1)[0]) for x in range(len(sortedDates)) if not sortedDates[x].__contains__("#")]

guardDict = {}
starts = [times[x] for x in range(len(times)) if (x & 1) == 0]
ends = [times[x] for x in range(len(times)) if (x & 1) == 1]

for i in range(len(numGuards)):
    guardDict[str(numGuards[i])] = []

guardCount, startEndCount = (-1,) * 2

for j in range(len(sortedDates)):
    if sortedDates[j].__contains__("wakes"):
        continue
    elif not sortedDates[j].__contains__("#"):
        startEndCount += 1
        guardDict[str(guardOrder[guardCount])].extend(list(range(starts[startEndCount], ends[startEndCount])))
    else:
        guardCount += 1

topArr = []
freq = []
for k in range(len(guardDict)):
    topArr.append([str(guardOrder[k]),
                   max(set(guardDict[str(guardOrder[k])]), key=guardDict[str(guardOrder[k])].count)])
    freq.append(guardDict[str(guardOrder[k])].count(
        max(set(guardDict[str(guardOrder[k])]), key=guardDict[str(guardOrder[k])].count)))

answer = int(topArr[freq.index(max(freq))][0]) * int(topArr[freq.index(max(freq))][1])

print(answer)
