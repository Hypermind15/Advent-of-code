import os, numpy

directory = os.path.dirname(os.path.abspath(__file__))
data = open(f"{directory}\\02 data.dat", "r")
reports = data.readlines()
data.close()

def isSafe(levels):
    sign = 0
    for i in range(len(levels) - 1):
        difference = int(levels[i + 1]) - int(levels[i])
        if abs(difference) < 1 or abs(difference) > 3:
            return False
        
        newSign = numpy.sign(difference)
        if newSign == -1 * sign:
            return False
            
        sign = newSign
    return True

numSafe = 0
numSafeWithOneRemoved = 0

for report in reports:
    levels = report.split()

    if isSafe(levels):
        numSafe += 1

    for i in range(len(levels)):
        levelsTmp = levels.copy()
        levelsTmp.pop(i)

        if isSafe(levelsTmp):
            numSafeWithOneRemoved += 1
            break

print("numSafe:", numSafe)
print("numSafeWithOneRemoved:", numSafeWithOneRemoved)