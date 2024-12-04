
searchPattern = "XMAS"
wordmap = []

def checkSafe(x,y, val):
    try:
        return wordmap[x][y] == val
    except IndexError:
        return None

def checkIfMAS(x,y):
    if checkSafe(x-1, y-1, 'M') and checkSafe(x+1, y+1, 'S') or checkSafe(x-1, y-1, 'S') and checkSafe(x+1, y+1, 'M'):
        if checkSafe(x-1, y+1, 'M') and checkSafe(x+1, y-1, 'S') or checkSafe(x-1, y+1, 'S') and checkSafe(x+1, y-1, 'M'):
            return True
    return False

with open("2024/inputs/04.txt", "r") as f:

    total_first = 0
    total_second = 0

    lines = f.readlines()

    for line in lines:
        wordmap.append(line.strip())

    # horizontal search
    for line in wordmap:
        total_first += line.count(searchPattern)
        line = line[::-1]
        total_first += line.count(searchPattern)

    # vertical search
    for i in range(len(wordmap[0])):
        line = [row[i] for row in wordmap]
        line = ''.join(line)
        total_first += line.count(searchPattern)
        line = line[::-1]
        total_first += line.count(searchPattern)

    # diagonal search /
    for i in range(1, len(wordmap[0]) * 2):

        cindex = abs(len(wordmap[0]) - i)
        if i < len(wordmap[0]):
            line = [wordmap[i + cindex][i] for i in range(len(wordmap) - cindex)]
        else:
            line = [wordmap[i][i + cindex] for i in range(len(wordmap) - cindex)]

        line = ''.join(line)

        total_first += line.count(searchPattern)
        line = line[::-1]
        total_first += line.count(searchPattern)

    # diagonal search \
    for i in range(1, len(wordmap[0]) * 2):

        cindex = abs(len(wordmap[0]) - i)
        if i < len(wordmap):
            line = [wordmap[i + cindex][len(wordmap) - 1 - i] for i in range(len(wordmap) - cindex)]

        else:
            line = [wordmap[i][len(wordmap) - 1 - i - cindex] for i in range(len(wordmap) - cindex)]

        line = ''.join(line)

        total_first += line.count(searchPattern)
        line = line[::-1]
        total_first += line.count(searchPattern)

    print(f"First answer: {total_first}")

    for i in range(1, len(wordmap[0])):
        for j in range(1, len(wordmap[0])):
            if wordmap[i][j] == "A" and checkIfMAS(i, j):
                total_second += 1
                
    print(f"Second answer: {total_second}")