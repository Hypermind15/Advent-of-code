import os, math, copy

directory = os.path.dirname(os.path.abspath(__file__))
data = open(f"{directory}\\06 test data.dat", "r")

mapOriginal = []
for line in enumerate(list(data.readlines())):
    mapRow = []
    for item in enumerate(list(line[1].rstrip("\n"))):
        #if item[1] == ".":
            #mapRow.append(None)
        if item[1] == "^":
            startPos = [item[0], line[0]]
            guardPos = [item[0], line[0]]
            mapRow.append("X")
        else:
            mapRow.append(item[1])
    
    mapOriginal.append(mapRow)
data.close()
print(*mapOriginal, sep="\n")
print(guardPos)


guardDirection = [0, -1] #x, y for next step. Coordinate grid starts in the top-left, so the guard starts facing up.


nextDirection = {
    ( 0, -1) : [ 1,  0],
    ( 1, 0 ) : [ 0,  1],
    ( 0, 1 ) : [-1,  0],
    (-1, 0 ) : [ 0, -1]
}

numLoopingPositions = 0

for extraObstaclePos0 in range(len(mapOriginal[0])):
    for extraObstaclePos1 in range(len(mapOriginal)):
        map = copy.deepcopy(mapOriginal)

        if map[extraObstaclePos0][extraObstaclePos1] != "#":

            map[extraObstaclePos0][extraObstaclePos1] = "#"
            print(extraObstaclePos0, extraObstaclePos1)

            finished = looped = False
            distinctSpacesVisited = 1

            while not finished and not looped:
                nextPos = [(guardPos[0] + guardDirection[0]), (guardPos[1] + guardDirection[1])]

                #Gone off end of map --> finished
                if (nextPos[0] < 0 or nextPos[0] >= len(map[0])) or (nextPos[1] < 0 or nextPos[1] >= len(map)):
                    finished = True

                #Hit an obstacle
                elif map[nextPos[1]][nextPos[0]] == "#": #Map has first index as y and second as x
                    guardDirection = nextDirection[tuple(guardDirection)]
                
                #Looped back to start
                elif nextPos == startPos and guardDirection == [0, -1]:
                    looped = True
                    numLoopingPositions += 1
                    print(*map, sep="\n")
                    print()

                #Space is empty
                else:
                    guardPos = nextPos.copy()
                    if map[guardPos[1]][guardPos[0]] != "X":
                        distinctSpacesVisited += 1
                        map[guardPos[1]][guardPos[0]] = "X"
    

    #print(*map, sep="\n")
    #print()

print(f"{numLoopingPositions=}")
print(f"{distinctSpacesVisited=}")