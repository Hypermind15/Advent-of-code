import os, time

#A recursive function that check if a location conatins a box, a wall or is empty
def CheckSquareAndMove(position, movingObject, direction):
    x = position[0]
    y = position[1]
    
    thingThere = map[y][x]
    match thingThere:
        #If it is a wall, nothing will move
        case "#":
            return False

        #If it is empty, it will cause the whole chain behind it to move
        case ".":
            map[y] = map[y][:x] + movingObject + map[y][(x + 1):]
            return True
        
        #If it is a box, it needs to check the next box, and will keep doing so until it finds a wall or empty space
        case "O":
            nextPosition = [(x + direction[0]), (y + direction[1])]
            boxMovable = CheckSquareAndMove(nextPosition, "O", direction)

            #If it is the box next to the robot and is moving, it moves the robot to where the box was.
            #If it is any other box, it will be replaced with another box
            if boxMovable:
                map[y] = map[y][:x] + movingObject + map[y][(x + 1):]
                return True
            
            return False


#--Main--
watchPlayback = True


directory = os.path.dirname(os.path.abspath(__file__))
data = open(f"{directory}\\15 test data.dat", "r")

#Converts directions into a usable form
directionLookup = {
    ">" : [ 1,  0],
    "<" : [-1,  0],

    "^" : [ 0, -1],
    "v" : [ 0,  1]
}

map = []
commands = ""
splitFound = False

#Formats the data in a usable form
for line in data.readlines():
    line = line.rstrip("\n")
    if line == "":
        splitFound = True
    else:
        if not splitFound:
            map.append(line)
        else:
            commands += line
data.close()

#Finds the robot
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "@":
            robotPosition = [x, y]

#Attempts to execute each command
for command in commands:
    direction = directionLookup[command]

    nextPos = [(robotPosition[0] + direction[0]), (robotPosition[1] + direction[1])]

    #If the robot has moved, replace its old position with an empty space
    canMove = CheckSquareAndMove(nextPos, "@", direction)
    if canMove:
        map[robotPosition[1]] = map[robotPosition[1]][:robotPosition[0]] + "." + map[robotPosition[1]][(robotPosition[0] + 1):]
        robotPosition = nextPos
    
    if watchPlayback and canMove:
        print(*map, sep="\n", end="\n\n\n\n\n")
        time.sleep(0.5)


#Calculates the sum of GPS coordinates for each box (100x distance from top + distance from left)
coordinateSum = 0
for line in list(enumerate(map)):
    for char in list(enumerate(line[1])):
        if char[1] == "O":
            coordinate = (100 * line[0]) + char[0]
            coordinateSum += coordinate


print(*map, sep="\n")
print(f"{coordinateSum=}")