
robots = []
mapsize = (101,103)

def getNewPos(robot):
    (posx, posy, vx, vy) = robot
    (maxX, maxY) = mapsize
    return ((posx + vx) % maxX, (posy + vy) % maxY)

def simulateStep():
    global robots
    newRobots = []
    for robot in robots:
        (_, _, vx, vy) = robot
        (newPosX, newPosY) = getNewPos(robot)
        newRobots.append((newPosX, newPosY, vx, vy))

    robots = newRobots

def countRobotsinQuadrants():
    (maxX, maxY) = mapsize
    quadrantXSize = maxX // 2
    quadrantYSize = maxY // 2

    leftU = 0
    leftD = 0
    rightU = 0
    rightD = 0

    for robot in robots:
        (posx, posy, _, _) = robot
        if posx < quadrantXSize:
            if posy < quadrantYSize:
                leftU += 1
            elif posy >= quadrantYSize + 1:
                leftD += 1
        elif posx >= quadrantXSize + 1:
            if posy < quadrantYSize:
                rightU += 1
            elif posy >= quadrantYSize + 1:
                rightD += 1

    return leftU * leftD * rightU * rightD

def printMap():
    (maxX, maxY) = mapsize
    for y in range(maxY):
        for x in range(maxX):
            count = 0
            for robot in robots:
                (posx, posy, _, _) = robot
                if x == posx and y == posy:
                    count += 1
            if count > 0:
                print(count, end="")
            else:
                print(".", end="")
        print("")


def calcVariance():
    n = len(robots)
    mean_x = sum(x for (x,_,_,_) in robots) / n
    mean_y = sum(y for (_,y,_,_) in robots) / n

    variance = sum(
        ((x - mean_x) ** 2 + (y - mean_y) ** 2) for (x,y,_,_) in robots
    ) / n
    
    return variance


def printMapToFile(file_path, i):
    (maxX, maxY) = mapsize
    with open(file_path, "a") as file:
        file.write(f"\n############################################### | {i} \n")
        for y in range(maxY):
            for x in range(maxX):
                count = 0
                for robot in robots:
                    (posx, posy, _, _) = robot
                    if x == posx and y == posy:
                        count += 1
                if count > 0:
                    file.write(str(count))
                else:
                    file.write(".")
            file.write("\n")


with open("2024/inputs/14.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line == "":
            continue

        line = line.split(" ")
        posx,posy = int(line[0].split(",")[0].split("=")[1]), int(line[0].split(",")[1])
        vx,vy = int(line[1].split(",")[0].split("=")[1]), int(line[1].split(",")[1])
        robots.append((posx, posy, vx, vy))

iterations = 20000 # easter egg should prob. be in the first 20000

for i in range(iterations):
    simulateStep()

    if i == 99:
        print(f"First answer: {countRobotsinQuadrants()}")

    variance = calcVariance()
    if variance < 1000: # maybe a bit too weak
        print(f"Second answer: {i+1}")
        break
        # print(i)
        # print("###################################################")
        # printMapToFile("output.txt", f"{i} | {calcVariance()}")


