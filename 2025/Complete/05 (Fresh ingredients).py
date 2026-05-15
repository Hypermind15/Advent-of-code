import os

directory = os.path.dirname(os.path.abspath(__file__))
data = open(f"{directory}\\05 data.dat", "r")

dataList = data.readlines()
data.close()

freshIDRanges = []
IDs = []

breakFound = False
for line in dataList:
    line = line.rstrip("\n")

    if line == "":
        breakFound = True
        continue

    if not breakFound:
        breakIndex = line.find("-")
        freshIDRanges.append([int(line[:breakIndex]), int(line[(breakIndex + 1):])])
    else:
        IDs.append(int(line))

print(IDs)
print(freshIDRanges)



#Part 1
numFreshAvailable = 0

for ID in IDs:
    for freshIDRange in freshIDRanges:
        if ID >= freshIDRange[0] and ID <= freshIDRange[1]:
            numFreshAvailable += 1

            break

print(numFreshAvailable)



#Part 2
totalNumfreshIDs = 0

for i in range(len(freshIDRanges)):
    print("-", freshIDRanges[i])

    if freshIDRanges[i] == -1:
        continue
    
    #Updates other ranges to not include this range
    for j in range(i + 1, len(freshIDRanges)):
        if freshIDRanges[j] == -1 or freshIDRanges[i] == -1:
            continue
        
        #If this one surrounds a later one
        if freshIDRanges[i][0] <= freshIDRanges[j][0] and freshIDRanges[i][1] >= freshIDRanges[j][1]:
            freshIDRanges[j] = -1
        
        #If a later one surrounds this one
        elif freshIDRanges[j][0] <= freshIDRanges[i][0] and freshIDRanges[j][1] >= freshIDRanges[i][1]:
            freshIDRanges[i] = -1
        
        elif freshIDRanges[i][0] >= freshIDRanges[j][0] and freshIDRanges[i][0] <= freshIDRanges[j][1]:
            freshIDRanges[j][1] = freshIDRanges[i][0] - 1
        
        elif freshIDRanges[i][1] >= freshIDRanges[j][0] and freshIDRanges[i][1] <= freshIDRanges[j][1]:
            freshIDRanges[j][0] = freshIDRanges[i][1] + 1

        
        print(freshIDRanges[j])
    

    #Adds the number of items in the current range to the total
    if freshIDRanges[i] != -1:
        totalNumfreshIDs += freshIDRanges[i][1] - freshIDRanges[i][0] + 1
        

print(totalNumfreshIDs)