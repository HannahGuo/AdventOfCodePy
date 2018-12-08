changes = [line.rstrip('\n') for line in open('input.txt')]

start = 0
freq = [0]

while True:
    for i in range(len(changes)):
        start += int(changes[i])
        if not freq.__contains__(start):
            freq.append(start)
        else:
            print(start)
            exit(0)
