import os, math, itertools

directory = os.path.dirname(os.path.abspath(__file__))
data = open(f"{directory}\\07 data.dat", "r")

validValueSum = 0

for line in data.readlines():
    line = line.split(":")

    target = int(line[0])

    nums = []
    for i in ((line[1].rstrip("\n")).split()):
        nums.append(int(i))

    for combination in list(itertools.product("+*|", repeat = (len(nums) - 1))):
        res = nums[0]
        for i in range(len(nums) - 1):
            if combination[i] == "+":
                res = res + nums[i + 1]
            elif combination[i] == "*":
                res = res * nums[i + 1]
            elif combination[i] == "|":
                res = int(str(res) + str(nums[i + 1]))
        if res == target:
            validValueSum += target
            break

print(f"{validValueSum=}")