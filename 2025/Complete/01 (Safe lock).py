import os

directory = os.path.dirname(os.path.abspath(__file__))
data = open(f"{directory}\\01 data.dat", "r")

moves = data.readlines()
data.close()

value = 50
totalNum0sA = 0 #Only when it stops at 0
totalNum0sB = 0 #When it passes 0

for move in moves:
    match move[0]:
        case "L":
            for i in range(int(move[1:])):
                value = (value - 1) % 100
                if value == 0:
                    totalNum0sB += 1
        case "R":
            for i in range(int(move[1:])):
                value = (value + 1) % 100
                if value == 0:
                    totalNum0sB += 1
    
    if value == 0:
        totalNum0sA += 1

print(totalNum0sA)
print(totalNum0sB)