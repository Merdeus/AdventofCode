from enum import Enum

class Field(Enum):
    OBSTACLE = 1
    VISITED = 2
    NOTVISITED = 3
    NONE = 4
    MARKER = 5

class Orientation(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


map = []
guardPosX = 0
guardPosY = 0

origGuardPosX = 0
origGuardPosY = 0

guardOrientation = Orientation.UP

visitesFields = set()

def getField(x,y):
    if x < 0 or y < 0:
        return Field.NONE
    try:
        return map[y][x]
    except IndexError:
        return Field.NONE

def getFieldFromChar(input : str) -> Field:
    if input == ".":
        return Field.NOTVISITED
    elif input == "#":
        return Field.OBSTACLE
    elif input == "X":
        return Field.VISITED
    elif input == "^":
        return Field.VISITED

def countVisitedFields():
    total = 0
    for _ in map:
        for x in _:
            if x == Field.VISITED:
                total += 1

    return total

def getOrientationDrawing():
    if guardOrientation == Orientation.UP:
        return "^"
    elif guardOrientation == Orientation.RIGHT:
        return ">"
    elif guardOrientation == Orientation.DOWN:
        return "v"
    elif guardOrientation == Orientation.LEFT:
        return "<"


DIRECTION_DELTAS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def wouldItCauseALoop():
    global guardPosX, guardPosY, guardOrientation

    check_visited = set()

    while True:

        fieldInFront = getFieldInFront()

        if fieldInFront == Field.OBSTACLE:
            guardOrientation = Orientation((guardOrientation.value % 4) + 1)
            continue
        elif fieldInFront == Field.NONE:
            return False

        if guardOrientation == Orientation.UP:
            guardPosY -= 1
        elif guardOrientation == Orientation.RIGHT:
            guardPosX += 1
        elif guardOrientation == Orientation.DOWN:
            guardPosY += 1
        else:
            guardPosX -= 1

        if (guardPosX, guardPosY, guardOrientation) in check_visited:
            return True
        check_visited.add((guardPosX, guardPosY, guardOrientation))


def printMap():
    for y in range(len(map)):
        for x in range(len(map[0])):
            if guardPosX == x and guardPosY == y and False:
                print(getOrientationDrawing(), end="")
            else:
                if map[y][x] == Field.NOTVISITED:
                    print(".", end="")
                elif map[y][x] == Field.VISITED:
                    print("X", end="")
                elif map[y][x] == Field.OBSTACLE:
                    print("#", end="")
                elif map[y][x] == Field.MARKER:
                    print("O", end="")
        print("")



def getFieldInFront():
    if guardOrientation == Orientation.UP:
        return getField(guardPosX, guardPosY - 1)
    elif guardOrientation == Orientation.RIGHT:
        return getField(guardPosX + 1, guardPosY)
    elif guardOrientation == Orientation.DOWN:
        return getField(guardPosX, guardPosY + 1)
    else:
        return getField(guardPosX - 1, guardPosY)

with open("2024/inputs/06.txt", "r") as f:

    lines = f.readlines()

    for index in range(len(lines)):
        lines[index] = lines[index].strip()

    for y in range(len(lines)):
        map.insert(y, [getFieldFromChar(char) for char in lines[y]])

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "^":
                guardPosX = x
                guardPosY = y
                origGuardPosX = x
                origGuardPosY = y

    # print("Before stepping:")
    # printMap()

    for step in range(50000):
        
        fieldInFront = getFieldInFront()

        if fieldInFront in [Field.VISITED, Field.NOTVISITED]:

            if guardOrientation == Orientation.UP:
                guardPosY -= 1
            elif guardOrientation == Orientation.RIGHT:
                guardPosX += 1
            elif guardOrientation == Orientation.DOWN:
                guardPosY += 1
            else:
                guardPosX -= 1

            map[guardPosY][guardPosX] = Field.VISITED
            visitesFields.add((guardPosX, guardPosY))

        elif fieldInFront == Field.OBSTACLE:
            guardOrientation = Orientation((guardOrientation.value % 4) + 1)
        else: # escaped
            break

    # print("")
    # print("")
    # print("After stepping:")

    # printMap()
    print(f"First answer: {countVisitedFields()}")


    total_second = 0
    second_marker = set([])

    for field in visitesFields:
    

        guardPosX = origGuardPosX
        guardPosY = origGuardPosY
        guardOrientation = Orientation.UP

        (fX, fY) = field

        if origGuardPosX == fX and origGuardPosY == fY:
            continue

        map[fY][fX] = Field.OBSTACLE
        if wouldItCauseALoop():
            second_marker.add((fX, fY))
            total_second += 1
        map[fY][fX] = Field.VISITED

    # for marker in second_marker:
    #     (fX, fY) = marker
    #     map[fY][fX] = Field.MARKER

    # printMap()

    print(f"Second answer: {total_second}")