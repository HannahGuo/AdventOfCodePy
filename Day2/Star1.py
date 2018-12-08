changes = [line.rstrip('\n') for line in open('input.txt')]

alpha = "abcdefghijklmnopqrstuvwxyz"
twoCount = []
# threeCount = []

threeCount = [i for i in range(len(alpha)) if changes[i].count(alpha[i]) == 3]
print(threeCount)


twoCount = [i for i in range(len(alpha)) if changes[i].count(alpha[i]) == 2 and not twoCount.__contains__(i)]

print(len(twoCount) * len(threeCount))