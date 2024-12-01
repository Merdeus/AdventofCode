
with open("2024/inputs/01.txt", "r") as f:

    leftNumbers = []
    rightNumbers = []

    for line in f:
        num = line.split("   ")

        if len(num) < 1:
            continue

        leftNumbers.append(int(num[0]))
        rightNumbers.append(int(num[1]))

    leftNumbers = sorted(leftNumbers)
    rightNumbers = sorted(rightNumbers)

    total_first = 0

    for i in range(len(leftNumbers)):
        total_first += abs(leftNumbers[i] - rightNumbers[i])

    print(f"First answer: {total_first}")

    occ_numbers = {}
    for num in rightNumbers:
        if num in occ_numbers:
            occ_numbers[num] += 1
        else:
            occ_numbers[num] = 1

    total_second = 0

    for num in leftNumbers:
        if num in occ_numbers:
            total_second += num * occ_numbers[num]
    
    print(f"Second answer: {total_second}")
