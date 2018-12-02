from difflib import SequenceMatcher
changes = [line.rstrip('\n') for line in open('input.txt')]
foundStr = []
sameStr = []

for i in range(len(changes)):
    for j in range(1, len(changes)):
        s = SequenceMatcher(None, changes[i], changes[j])
        if s.ratio() > (24 / 26) and changes[i] != changes[j]:
            foundStr.append("".join(changes[i]))
            foundStr.append("".join(changes[j]))
            for k in range(len(changes[0])):
                if foundStr[0][k] in foundStr[1]:
                    sameStr.append(foundStr[0][k])
            print("".join(sameStr))
            exit()
