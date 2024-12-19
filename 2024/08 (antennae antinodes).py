import os, itertools

directory = os.path.dirname(os.path.abspath(__file__))
data = open(f"{directory}\\08 data.dat", "r")

dataLines = data.readlines()
data.close()

antennae = {}
for line in list(enumerate(dataLines)):
    dataLines[line[0]] = dataLines[line[0]].rstrip("\n")

    for char in list(enumerate(line[1].rstrip("\n"))):
        if char[1] != ".":
            if char[1] in antennae.keys():
                antennae[char[1]].append([line[0], char[0]])

            else:
                antennae.update({char[1] : [[line[0], char[0]]]})


numAntinodeLocations = 0

dataLinesCopy = dataLines.copy()

for frequency in antennae.keys():
    print(frequency, antennae[frequency])
    if len(antennae[frequency]) > 1:
        #Loops through each combination of 2 antennae
        for posCombination in itertools.combinations(antennae[frequency], 2):
            print(posCombination)

            #dy/dx
            inlineM =  (posCombination[0][0] - posCombination[1][0]) / (posCombination[0][1] - posCombination[1][1])

            #y-intercept (=y1 - m(x1))
            inLineC = posCombination[0][0] - inlineM * posCombination[0][1]

            for y in range(len(dataLines)):
                for x in range(len(dataLines[y])):

                    #Checks if the position is in line with the towers
                    if inlineM * x + inLineC == y:
                        print(y, x, "In line")

                        #If it is 2x the distance from posCombination[0] and posCombination[1] OR 2x the distance from posCombination[1] and posCombination[0]
                        distance1 = [(y - posCombination[0][0]), (x - posCombination[0][1])]
                        distance2 = [(y - posCombination[1][0]), (x - posCombination[1][1])]

                        squareDistance1 = (distance1[1] ** 2) + (distance1[0] ** 2)
                        squareDistance2 = (distance2[1] ** 2) + (distance2[0] ** 2)

                        print(squareDistance1, squareDistance2)

                        if (squareDistance1 == 4 * squareDistance2) or (4 * squareDistance1 == squareDistance2):
                            print(frequency)
                            if dataLinesCopy[y][x] != "frequency" and dataLines[y][x] != "#":
                                dataLines[y] = dataLines[y][:x] + "#" + dataLines[y][(x + 1):]

                                numAntinodeLocations += 1
                    
print(*dataLines, sep="\n")
print()
print(*dataLinesCopy, sep="\n")

print(f"{numAntinodeLocations=}")