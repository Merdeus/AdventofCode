# not proud of this one. The choosen approach is definitly not the best one.
# Code looks weird because I have switched approach multiple times while
# writing the code because I was not sure how to solve part 2

map = []
processed_tiles = set()

def grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            yield x, y

def getByIndex(y,x):
    if x < 0 or y < 0:
        return None

    try:
        return map[y][x]
    except IndexError:
        return None

def FindNextUnusedTile():
    for x,y in grid(map):
        if (y,x) in processed_tiles:
            continue
        return (y,x)
    return None

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def getAllTilesOfArea(y : int, x : int, current):

    for (dy,dx) in dirs:
        ty = y+dy
        tx = x+dx
        t = getByIndex(ty, tx)

        if not t:
            continue

        if t != getByIndex(y,x):
            continue

        if (ty,tx) in current:
            continue

        processed_tiles.add((ty,tx))
        current.add((ty,tx))
        current = getAllTilesOfArea(ty,tx,current)

    return current

def getAmountOfFriendlySurroundingTiles(y,x):
    total = 0
    cur = getByIndex(y, x)
    for (dy,dx) in dirs:
        ty = y+dy
        tx = x+dx
        t = getByIndex(ty, tx)

        if t == cur:
            total += 1

    return total


def getAmountOfFenceOfArea(areaSet):

    total = 0
    for (cy,cx) in areaSet:
        total += (4 - getAmountOfFriendlySurroundingTiles(cy,cx))

    return total

def returnAmountofLinesinSet(input : set):

    result = 0

    while True:

        if len(input) < 1:
            break

        for c in input:
            current = c
            break

        current_processed = set([current])
        
        prevSize = 0

        while len(current_processed) != prevSize:
            new_current_processed = set([])
            prevSize = len(current_processed)
            for m in current_processed:
                for other in input:
                    if other in current_processed:
                        continue
                    
                    (cy, cx) = m
                    (oy, ox) = other
        
                    if (abs(cy-oy) + abs(cx-ox)) == 1:
                        new_current_processed.add(other)

            for new in new_current_processed:
                current_processed.add(new)

        result += 1
        for c in current_processed:
            input.remove(c)

    return result


def getAmountOfFenceSides(areaSet):

    boundary_tiles = set()
    for (y, x) in areaSet:
        for dy, dx in dirs:
            neighbor = (y + dy, x + dx)
            if neighbor not in boundary_tiles:
                boundary_tiles.add((y, x))
                break

    result = 0

    horizontal_up = set([])
    vertical_left = set([])
    horizontal_down = set([])
    vertical_right = set([])

    # determine if it is a horizontal or vertical boundary, or both?
    for tile in boundary_tiles:

        left = True
        right = True
        down = True
        up = True

        (y, x) = tile
        for (dy, dx) in dirs:
            neighbor = (y + dy, x + dx)
            if neighbor in areaSet:
                if dy != 0:
                    if dy == -1:
                        up = False
                    else:
                        down = False
                else:
                    if dx == -1:
                        left = False
                    else:
                        right = False

        if left:
            vertical_left.add((y, x))
        if right:
            vertical_right.add((y, x))
        if up:
            horizontal_up.add((y, x))
        if down:
            horizontal_down.add((y, x))

    for c in [vertical_left, vertical_right, horizontal_up, horizontal_down]:
        result += returnAmountofLinesinSet(c)

    return result


with open("2024/inputs/12.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()

        if line == "":
            continue

        map.append([a.strip() for a in line])


total_first = 0
total_second = 0

while True:
    c = FindNextUnusedTile()
    if not c:
        #print("Finished!")
        break

    (cy,cx) = c
    carea = getAllTilesOfArea(cy,cx, set([(cy,cx)]))
    processed_tiles.add((cy,cx))
    amountFence = getAmountOfFenceOfArea(carea)
    amountDistinctSideFencesIdk = getAmountOfFenceSides(carea)

    total_first += amountFence * len(carea)
    total_second += amountDistinctSideFencesIdk * len(carea)


print(f"First answer: {total_first}") 
print(f"Second answer: {total_second}")