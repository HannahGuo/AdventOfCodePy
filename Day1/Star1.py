changes = [line.rstrip('\n') for line in open('input.txt')]

print(sum(int(changes[i]) for i in range(len(changes))))
