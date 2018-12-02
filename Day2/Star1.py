changes = [line.rstrip('\n') for line in open('input.txt')]

twoCount = []
threeCount = []
alpha = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(changes)):
    changes[i] = list(changes[i])
    changes[i].sort()

    for j in range(len(alpha)):
        if changes[i].count(alpha[j]) == 3 and not threeCount.__contains__(i):
            threeCount.append(i)
        if changes[i].count(alpha[j]) == 2 and not twoCount.__contains__(i):
            twoCount.append(i)

print(len(twoCount) * len(threeCount))