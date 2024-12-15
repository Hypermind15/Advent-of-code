import os

directory = os.path.dirname(os.path.abspath(__file__))
data = open(f"{directory}\\03 data.dat", "r")

dataLines = data.readlines()
data.close()
data = "".join(dataLines)

multiplySeries = ["m", "u", "l", "(", None, ",", None, ")"]
startSeries = ["d", "o", "(", ")"]
endSeries = ["d", "o", "n", "'", "t", "(", ")"]

productSum = 0

enabled = True

for i in range(len(data)):
    matchCounter = 0
    dataCounter = 0

    if data[i] == multiplySeries[matchCounter]:
        if enabled:
            print("m found")
            matching = notFinished = True
            commaFound = False
            num1 = ""
            num2 = ""

            matchCounter += 1
            dataCounter += 1
            while matching and notFinished:
                #print("m:", matchCounter, "     d:", dataCounter)
                if multiplySeries[matchCounter] == None:
                    try:
                        int(data[i + dataCounter])

                        #print("num found")
                        if not commaFound:
                            num1 += data[i + dataCounter]
                        else:
                            num2 += data[i + dataCounter]
                        dataCounter += 1
                    except:
                        matchCounter += 1
                    
                elif data[i + dataCounter] != multiplySeries[matchCounter]:
                    matching = False
                
                elif multiplySeries[matchCounter] == ",":
                    matchCounter += 1
                    dataCounter += 1

                    commaFound = True

                    print("comma found")
                else:
                    matchCounter += 1
                    dataCounter += 1
                
                if matchCounter > 7:
                    notFinished = False
                
            if matching:
                #print(f"num1: {num1}        num2: {num2}")
                product = int(num1) * int(num2)
                productSum += product
    
    elif data[i] == startSeries[matchCounter]:
        matching = True
        startCommand = True

        while matching:
            matchCounter += 1

            if matchCounter >= len(startSeries) and startCommand:
                enabled = True
                break
            if matchCounter >= len(endSeries) and not startCommand:
                enabled = False
                break

            if matchCounter == 1:
                if data[i + matchCounter] != startSeries[matchCounter]:
                    matching = False
            elif matchCounter == 2:
                if data[i + matchCounter] == endSeries[matchCounter]:
                    startCommand = False
            else:
                if startCommand:
                    if data[i + matchCounter] != startSeries[matchCounter]:
                        matching = False
                else:
                    if data[i + matchCounter] != endSeries[matchCounter]:
                        matching = False
            

print(f"Sum of products: {productSum}")