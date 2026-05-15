import os

directory = os.path.dirname(os.path.abspath(__file__))
data = open(f"{directory}\\06 data.dat", "r")

lines = [line.rstrip("\n") for line in data.readlines()]
data.close()


def removeAll(list, itemToRemove):
    newList = []
    for item in list:
        if item != itemToRemove:
            newList.append(item)

    return newList


def product(numArray):
    product = 1
    for num in numArray:
        product *= num
    return product



#PART 1
operands = []

for i in range(len(lines) - 1):
    operands.append(removeAll((lines[i]).split(" "), ""))

operators = removeAll((lines[-1]).split(" "), "")


total = 0
#Computes sums
for i in range(len(operators)):
    sumOrProduct = (0 if operators[i] == "+" else 1)

    for operandList in operands:
        if operators[i] == "+":
            sumOrProduct += int(operandList[i])
        if operators[i] == "*":
            sumOrProduct *= int(operandList[i])

    total += sumOrProduct

print(total)



#Part 2
columns = [[None for i in range(len(lines))] for j in range(len(lines[0]))]
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        columns[j][i] = char


#Removes columns that are all blank spaces
columns = removeAll(columns, [' '] * len(lines))


total = 0
tempColumns = []
currentOperation = ""

#Computes the sums
for col in columns:
    if col[-1] != ' ':
        #Computes the current sum / product
        if currentOperation == "+":
            total += sum(tempColumns)
            print(sum(tempColumns))
        if currentOperation == "*":
            total += product(tempColumns)
            print(product(tempColumns))

        currentOperation = col[-1]
        tempColumns.clear()
    
    tempColumns.append(int("".join(col[:-1])))

#Computes the last sum / product
if currentOperation == "+":
    total += sum(tempColumns)
    print(sum(tempColumns))
if currentOperation == "*":
    total += product(tempColumns)
    print(product(tempColumns))
    

print(total)