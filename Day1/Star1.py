changes = [line.rstrip('\n') for line in open('input.txt')]

start = 0

for i in range(len(changes)):
    start += int(changes[i])

print(start)
