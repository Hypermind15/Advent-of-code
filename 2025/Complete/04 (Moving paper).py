import os

directory = os.path.dirname(os.path.abspath(__file__))
data = open(f"{directory}\\04 data.dat", "r")

rows = data.readlines()
#Converts string to list
for i, row in enumerate(rows):
    rows[i] = [i for i in row]
data.close()


numRows = len(rows)
numColumns = len(rows[0])

requiredChecks = [(0, 1), (0, -1), (1, 1), (1, 0), (1, -1), (-1, -1), (-1, 0), (-1, 1)]

numFreeRolls = 0
numRollsRemoved = -1
totalRollsRemoved = 0

firstPass = True

while numRollsRemoved != 0:
    numRollsRemoved = 0


    for i, row in enumerate(rows):
        for j, column in enumerate(row):
            #Only checks rolls, not spaces
            if column != "@":
                continue

            numAdjacentRolls = 0

            for check in requiredChecks:
                #Checks for edges so no errors
                
                if (i + check[0] in range(numRows)) and (j + check[1] in range(numColumns - 1)):
                    if rows[i + check[0]][j + check[1]] == "@":
                        numAdjacentRolls += 1
            

            if numAdjacentRolls < 4:
                #Remove the roll
                rows[i][j] = "."
                numRollsRemoved += 1

            #Part 1 ish
            if firstPass:
                numFreeRolls += int(numAdjacentRolls < 4)
                firstPass = False
    
    print(numRollsRemoved)
    totalRollsRemoved += numRollsRemoved


print(totalRollsRemoved)