import os, re

directory = os.path.dirname(os.path.abspath(__file__))
data = open(f"{directory}\\04 data.dat", "r")

wordsearchLines = data.readlines()
for i in range(len(wordsearchLines)):
    wordsearchLines[i] = wordsearchLines[i].rstrip("\n")
data.close()


#Part 1

wordsearchCols = [""] * len(wordsearchLines[0])
for col in range(len(wordsearchLines[0])):
    for row in range(len(wordsearchLines)):
        item = wordsearchLines[row][col]
        wordsearchCols[col] += item

print(wordsearchLines)

#Tests for top-left / diagonals
wordsearchDiags11 = [""] * len(wordsearchLines)
for i in range(len(wordsearchLines)):
    for j in range(i + 1):
        vertIndex  = j
        horizIndex = i - j
        wordsearchDiags11[i] += wordsearchLines[horizIndex][vertIndex]

#Tests for bottom-right / diagonals
wordsearchDiags12 = [""] * (len(wordsearchLines) - 1)
for i in range(len(wordsearchLines) - 1):
    for j in range(i + 1):
        vertIndex  = j
        horizIndex = i - j
        wordsearchDiags12[-(1 + i)] += wordsearchLines[-(1 + horizIndex)][-(1 + vertIndex)]

#print(wordsearchDiags11)
#print(wordsearchDiags12)

#Tests for bottom-left \ diagonals
wordsearchDiags21 = [""] * len(wordsearchLines)
for i in range(len(wordsearchLines)):
    for j in range(i + 1):
        vertIndex  = j
        horizIndex = i - j
        wordsearchDiags21[i] += wordsearchLines[-(1 + horizIndex)][vertIndex]

#Tests for top-right \ diagonals
wordsearchDiags22 = [""] * (len(wordsearchLines) - 1)
for i in range(len(wordsearchLines) - 1):
    for j in range(i + 1):
        vertIndex  = j
        horizIndex = i - j
        wordsearchDiags22[-(1 + i)] += wordsearchLines[horizIndex][-(1 + vertIndex)]

#print(wordsearchDiags21)
#print(wordsearchDiags22)



listsToSearch = [wordsearchLines, wordsearchCols, wordsearchDiags11, wordsearchDiags12, wordsearchDiags21, wordsearchDiags22]

totalMatches = 0
for list in listsToSearch:
    typeMatches = 0
    for item in list:
        matches = item.count("XMAS") + item.count("SAMX")
        typeMatches += matches
        totalMatches += matches
    print(typeMatches)

print(f"totalXMASMatches: {totalMatches}")


#Part 2

numCrossMASs = 0
for i in range(len(wordsearchLines)):
    for j in range(len(wordsearchLines[i])):
        if wordsearchLines[i][j] == "A":
            #Check it sint right on the edge
            if (i > 0 and i < len(wordsearchLines) - 1) and (j > 0 and j < len(wordsearchLines[i]) - 1):
                diag1 = "".join([wordsearchLines[i - 1][j - 1], wordsearchLines[i + 1][j + 1]])
                diag2 = "".join([wordsearchLines[i - 1][j + 1], wordsearchLines[i + 1][j - 1]])
                
                allowedDiagonals = ["MS", "SM"]
                if diag1 in allowedDiagonals and diag2 in allowedDiagonals:
                    numCrossMASs += 1
                    print(diag1)

print(f"{numCrossMASs=}")