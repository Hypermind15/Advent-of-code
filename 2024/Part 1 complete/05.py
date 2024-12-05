import os

directory = os.path.dirname(os.path.abspath(__file__))
data = open(f"{directory}\\05 data.dat", "r")

orderingRules = []
updates = []

#Breaks the data into 2 lists for the rules and the data
foundBreak = False
for line in data:
    if line == "\n":
        foundBreak = True
    
    if not foundBreak:
        orderingRules.append([int(line[0:2]), int(line[3:5])])
    
    elif line != "\n":
        update = line.split(",")

        if "\n" in update[-1]:
            update[-1] = update[-1][0:2]
        for i in range(len(update)):
            update[i] = int(update[i])
        
        updates.append(update)
data.close()


middleNumberSum = 0

for update in updates:
    correctOrder = True
    for item in list(enumerate(update)):
        print(item)
        for rule in orderingRules:
            #If the rule is relevant
            if rule[1] == item[1]:
                if rule[0] in update[item[0]:]:
                    correctOrder = False
                    print("Invalid")

    #Part 1      
    if correctOrder:
        print("Valid")
        middleNumber = update[int(len(update) / 2)]
        middleNumberSum += middleNumber
    
    #Part 2
    else:
        pass


print(f"{middleNumberSum=}")