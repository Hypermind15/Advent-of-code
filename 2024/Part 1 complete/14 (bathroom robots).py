import os, math

class Robot:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
    
    def updatePos(self, gridSize):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        if self.position[0] > gridSize[0] - 1:
            self.position[0] = self.position[0] - gridSize[0]
        elif self.position[0] < 0:
            self.position[0] = self.position[0] + gridSize[0]
        if self.position[1] > gridSize[1] - 1:
            self.position[1] = self.position[1] - gridSize[1]
        elif self.position[1] < 0:
            self.position[1] = self.position[1] + gridSize[1]


def ParseLine(line):
    parts = line.split()
    yield (parts[0].lstrip("p=")).split(",")
    yield (parts[1].lstrip("v=").rstrip("\n")).split(",")


def CountQuadrants(robots, gridSize):
    middleX = math.ceil((gridSize[0] - 1) / 2)
    middleY = math.ceil((gridSize[1] - 1) / 2)

    quadrants = [0] * 4
    for robot in robots:
        if robot.position[0] < middleX and robot.position[1] < middleY:
            quadrants[0] += 1
        if robot.position[0] > middleX and robot.position[1] < middleY:
            quadrants[1] += 1
        if robot.position[0] < middleX and robot.position[1] > middleY:
            quadrants[2] += 1
        if robot.position[0] > middleX and robot.position[1] > middleY:
            quadrants[3] += 1
    
    return quadrants


#Main

directory = os.path.dirname(os.path.abspath(__file__))
data = open(f"{directory}\\14 data.dat", "r")

robots = []
for line in data:
    parsedLine = list(ParseLine(line))

    position = list(map(int, parsedLine[0]))
    velocity = list(map(int, parsedLine[1]))

    robots.append(Robot(position, velocity))
data.close()


gridSize = (101, 103)

numTicks = 100
for tickNum in range(numTicks):
    for robot in robots:
        robot.updatePos(gridSize)

safetyFactor = math.prod(CountQuadrants(robots, gridSize))

#print(CountQuadrants(robots, gridSize))
#print(*(robot.position for robot in robots))

print(f"{safetyFactor=}")