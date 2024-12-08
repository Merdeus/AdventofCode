map = []
antinode_locations_1 = set()
antinode_locations_2 = set()
antenna_locations = {}

def isInBounds(y : int, x : int):

    if y < 0 or x < 0:
        return False

    try:
        map[y][x]
        return True
    except IndexError:
        return False


def printMap():
    for y in range(len(map)):
        for x in range(len(map[0])):
            if (y, x) in antinode_locations_1:
                print("#", end="")
            else:
                print(map[y][x], end="")
        print("")


with open("2024/inputs/08.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        map.append([char for char in line])


for y in range(len(map)):
    for x in range(len(map[0])):
        
        char = map[y][x]

        if char == '.':
            continue

        if char not in antenna_locations:
            antenna_locations[char] = set()

        antenna_locations[char].add((y,x))


for y in range(len(map)):
    for x in range(len(map[0])):

        char = map[y][x]
        if char == '.':
            continue
        
        locs = antenna_locations[char]

        for loc in locs:
            (ty, tx) = loc
            if y == ty and x == tx:
                continue

            tmp_y = y - (ty - y)
            tmp_x = x - (tx - x)

            if isInBounds(tmp_y, tmp_x):
                antinode_locations_1.add((tmp_y, tmp_x))

            tmp_y = y - (ty + y)
            tmp_x = x - (tx + x)

            if isInBounds(tmp_y, tmp_x):
                antinode_locations_1.add((tmp_y, tmp_x))


        for loc in locs:
            (ty, tx) = loc
            if y == ty and x == tx:
                continue

            factor = 0
            while True:
                tmp_y = y - ((ty - y) * factor)
                tmp_x = x - ((tx - x) * factor)

                if isInBounds(tmp_y, tmp_x):
                    antinode_locations_2.add((tmp_y, tmp_x))
                else:
                    break

                factor += 1

            factor = 0
            while True:
                tmp_y = y - ((ty + y) * factor)
                tmp_x = x - ((tx + x) * factor)

                if isInBounds(tmp_y, tmp_x):
                    antinode_locations_2.add((tmp_y, tmp_x))
                else:
                    break

                factor += 1


print(f"First answer: {len(antinode_locations_1)}")
print(f"Second answer: {len(antinode_locations_2)}")