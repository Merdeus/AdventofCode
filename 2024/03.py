import re

pattern = r"(?:mul\(\d+,\d+\)|do\(\)|don't\(\))"

with open("2024/inputs/03.txt", "r") as f:

    mul_enabled = True
    total_first = 0
    total_second = 0

    results = re.findall(pattern, f.read())

    for current in results:
        if current == "do()":
            mul_enabled = True
        elif current == "don't()":
            mul_enabled = False
        else:
            current = current[4:-1]
            current = current.split(",")
            first, second = int(current[0]), int(current[1])

            total_first += first * second
            if mul_enabled:
                total_second += first * second

    print(f"First answer: {total_first}")
    print(f"Second answer: {total_second}")