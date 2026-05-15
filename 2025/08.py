import os

directory = os.path.dirname(os.path.abspath(__file__))
data = open(f"{directory}\\08 data.dat", "r")

moves = [line.rstrip("\n") for line in data.readlines()]
data.close()