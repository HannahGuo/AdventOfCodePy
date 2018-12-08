inputText = [line.rstrip('\n') for line in open('input.txt')]

sortedDates = sorted(inputText)

guardOrder = [sortedDates[x].split("#")[1].split(" ", 1)[0] for x in range(len(sortedDates))
              if sortedDates[x].__contains__("#")]

numGuards = list(set(guardOrder))

times = [int(sortedDates[x].split(":")[1].split("]", 1)[0]) for x in range(len(sortedDates))
         if not sortedDates[x].__contains__("#")]

guardDict = {}
starts = [times[x] for x in range(len(times)) if (x & 1) == 0]
ends = [times[x] for x in range(len(times)) if (x & 1) == 1]

for i in range(len(numGuards)):
    guardDict[str(numGuards[i])] = []

guardCount, startEndCount = (-1,) * 2

for j in range(len(sortedDates)):
    if sortedDates[j].__contains__("wakes"):
        continue
    elif not sortedDates[n].__contains__("#"):
        startEndCount += 1
        guardDict[str(guardOrder[guardCount])].extend(list(range(starts[startEndCount], ends[startEndCount])))
    else:
        guardCount += 1

sleepyHead = int(max(guardDict, key=lambda x: len(guardDict[x])))
sleepyMinute = int(max(set(guardDict[str(sleepyHead)]), key=guardDict[str(sleepyHead)].count))
print(sleepyHead * sleepyMinute)
