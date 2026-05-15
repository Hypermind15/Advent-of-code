import os

def IsSequenceRepeatedTwice(ID):
    length = len(ID)

    if length % 2 == 1:
        return False
    
    return ID[:length // 2] == ID[length // 2:]


def IsSequenceRepeatedAtLeastTwice(ID):
    length = len(ID)

    for repeatLengthCheck in range(1, length // 2 + 1):
        #If it is a factor of length, check it
        if (length / repeatLengthCheck) == length // repeatLengthCheck:
            #print(repeatLengthCheck)
            flag = True
            for i in range(1, length // repeatLengthCheck):
                #print(ID[((i - 1) * repeatLengthCheck) : (i * repeatLengthCheck)], ID[(i * repeatLengthCheck) : ((i + 1) * repeatLengthCheck)])
                if ID[((i - 1) * repeatLengthCheck) : (i * repeatLengthCheck)] != ID[(i * repeatLengthCheck) : ((i + 1) * repeatLengthCheck)]:
                    flag = False

            
            if flag: return True
    
    return False
        

print(IsSequenceRepeatedAtLeastTwice("824824824"))


directory = os.path.dirname(os.path.abspath(__file__))
data = open(f"{directory}\\02 data.dat", "r")

IDRanges = data.readline().split(",")
data.close()

sumInvalid = 0

for IDRange in IDRanges:
    bounds = [int(i) for i in IDRange.split("-")]
    
    for ID in range(bounds[0], bounds[1] + 1):
        #if IsSequenceRepeatedTwice(str(ID)): PART 1
        if IsSequenceRepeatedAtLeastTwice(str(ID)):
            sumInvalid += ID

print(sumInvalid)