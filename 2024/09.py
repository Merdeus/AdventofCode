# This can be done much more efficently but it works

gdata = []

# add caching of latest empty block so you don't have to go through the entire list each time
def findEarliestEmptyBlockIndex(start = 0):
    for blockIndex in range(start, len(gdata)):
        if gdata[blockIndex] == -1:
            return blockIndex
    return None

def orderData_Part1():
    for c in range(len(gdata) - 1, 0, -1):
        if gdata[c] != -1:
            newBlockIndex = findEarliestEmptyBlockIndex()
            if newBlockIndex - 1 == c:
                break
            gdata[newBlockIndex], gdata[c] = gdata[c], -1

def doesitFit(startingIndex, length, d):
    
    currentLength = 0
    while True:
        if gdata[startingIndex + currentLength] == -1:
            currentLength += 1
        else:
            break
    if currentLength >= length:
        return True
    return False


def orderData_part2():

    # python actually does remember the loop variable and you can't just set
    # the for loop variable inside the loop to something else.

    c = len(gdata) - 1
    while c >= 0:
        if gdata[c] != -1:

            if c-1 < 0:
                break

            length = 1
            while True:
                if gdata[c] == gdata[c-1]:
                    c -= 1
                    length += 1
                else:
                    break

            currentFitting = 0
            while True:
                newBlockIndex = findEarliestEmptyBlockIndex(currentFitting)
                if newBlockIndex > c:
                    break

                if doesitFit(newBlockIndex, length, gdata[c]):
                    for i in range(length):
                        gdata[newBlockIndex + i], gdata[c + i] = gdata[c + i], -1
                    break
                currentFitting = newBlockIndex + 1

        c -= 1
                    

def calcChecksum():
    total = 0
    for i in range(len(gdata)):
        if gdata[i] == -1:
            continue
        total += (i * gdata[i])
    return total

with open("2024/inputs/09.txt", "r") as f:
    data = f.read()
    isData = True
    currentID = 0
    for char in data:
        char = char.strip()
        if char == "":
            continue
        for i in range(int(char)):
            if isData:
                gdata.append(currentID)
            else:
                gdata.append(-1) # represents free block
        
        if isData:
            currentID += 1
        isData = not isData

    orig_data = gdata.copy()
    orderData_Part1()
    print(f"First answer: {calcChecksum()}")
    gdata = orig_data
    #print(gdata)
    orderData_part2()
    #print(gdata)
    print(f"Second answer: {calcChecksum()}")