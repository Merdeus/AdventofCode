from functools import lru_cache

# if maxsize is not defined directly to None it defaults to 128...
@lru_cache(maxsize=None)
def getNumerOfStones(stone, depth):

    if depth == 0:
        return 1

    if stone == 0:
        return getNumerOfStones(1, depth-1)

    num_str = str(stone)
    num_length = len(num_str)    

    if num_length % 2 == 0:
        mid = num_length // 2
        return getNumerOfStones(int(num_str[:mid]), depth-1) + getNumerOfStones(int(num_str[mid:]), depth-1)
    else:
        return getNumerOfStones(stone * 2024, depth-1)


with open("2024/inputs/11.txt", "r") as f:
    data = f.read()
    data = data.strip()
    data = [int(s.strip()) for s in data.split(" ")]

    result = 0
    for stone in data:
        result += getNumerOfStones(stone, 25)
    print(f"First answer: {result}")

    result = 0
    for stone in data:
        result += getNumerOfStones(stone, 75)
    print(f"Second answer: {result}")