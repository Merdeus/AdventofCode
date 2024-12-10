map = []

total_first = 0
total_second = 0

# up, right, down, left
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def getByIndex(y,x):
    if x < 0 or y < 0:
        return None

    try:
        return map[y][x]
    except IndexError:
        return None

def addValues(tbl1, tbl2):
    for key in tbl2.keys():
        if key in tbl1:
            tbl1[key] += tbl2[key]
        else:
            tbl1[key] = tbl2[key]
    return tbl1

def grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            yield x, y

def getTrailheads():

    results = []
    for x,y in grid(map):
        p = getByIndex(y,x)
        if p == 0:
            results.append((y,x))
    return results

def getEndPoints(currentLevel, y, x):

    endpoints = set()

    if currentLevel == 9:
        endpoints.add((y,x))
        return endpoints

    for (vy,vx) in dirs:
        ty = y - vy
        tx = x - vx
        field = getByIndex(ty, tx)
        if field == currentLevel + 1:
            endpoints = endpoints.union(getEndPoints(currentLevel + 1, ty, tx))

    return endpoints

def getEndPoints2(currentLevel, y, x):

    endpoints = dict()

    if currentLevel == 9:
        return (y,x)

    for (vy,vx) in dirs:
        ty = y - vy
        tx = x - vx
        field = getByIndex(ty, tx)
        if field == currentLevel + 1:
            tmp = getEndPoints2(currentLevel + 1, ty, tx)

            if isinstance(tmp, tuple):
                if tmp in endpoints:
                    endpoints[tmp] += 1
                else:
                    endpoints[tmp] = 1
            else:
                endpoints = addValues(endpoints, tmp)

    return endpoints


with open("2024/inputs/10.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()

        if line == "":
            continue

        map.append([int(a) for a in line])


trailheads = getTrailheads()
for (py,px) in trailheads:

    total_first += len(getEndPoints(0,py,px))

    t = getEndPoints2(0,py,px)
    for endpoint in t:
        total_second += t[endpoint]

print(f"First answer: {total_first}")
print(f"Second answer: {total_second}")
