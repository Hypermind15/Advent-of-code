import os

directory = os.path.dirname(os.path.abspath(__file__))
data = open(f"{directory}\\03 data.dat", "r")

banks = data.readlines()
data.close()


def FindFirstMaxJoltage(bank, digitNumber): #For digitNumber, 0 = 1s column, 1 = 10s column etc
    max = -1
    maxIndex = 0

    for i, joltage in enumerate(bank[:(len(bank) - digitNumber)]):
        if int(joltage) > max:
            max = int(joltage)
            maxIndex = i
    
    return max * (10 ** digitNumber), maxIndex

numDigitsWanted = 12

totalMax = 0

for bank in banks:
    bank = bank.rstrip("\n")
    thisBankNumber = 0

    for digit in range(numDigitsWanted - 1, -1, -1):
        firstMaxJoltage, firstMaxIndex = FindFirstMaxJoltage(bank, digit)
        bank = bank[(firstMaxIndex + 1):]

        thisBankNumber += firstMaxJoltage

    totalMax += thisBankNumber

print(totalMax)