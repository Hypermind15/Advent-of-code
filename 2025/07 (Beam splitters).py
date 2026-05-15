import os

def SumDictionaryValues(dict):
    sum = 0

    for value in dict.values():
        sum += int(value)

    return sum


directory = os.path.dirname(os.path.abspath(__file__))
data = open(f"{directory}\\07 data.dat", "r")

lines = [line.rstrip("\n") for line in data.readlines()]
data.close()

beamCols = {lines[0].find("S") : 1}

numSplits = 0
for i, line in enumerate(lines[1:]):
    for j, item in enumerate(line):
        if item == "^" and j in beamCols:
            #Part 1
            numSplits += 1

            #Part 2
            if j - 1 in beamCols: beamCols[j - 1] += beamCols[j]
            else: beamCols.update({j - 1 : beamCols[j]})

            if j + 1 in beamCols: beamCols[j + 1] += beamCols[j]
            else: beamCols.update({j + 1 : beamCols[j]})

            beamCols.pop(j)
    
    print("".join([str(beamCols[t]) if t in beamCols else "." for t in range(len(line)) ]))

            
print(numSplits)
print(SumDictionaryValues(beamCols))