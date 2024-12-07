from itertools import product

from enum import Enum

class Operation(Enum):
    ADD = 1
    MUL = 2
    CON = 3


def generate_permutations(n, ops = [Operation.ADD, Operation.MUL]):

    if n <= 0:
        return []
    return [list(comb) for comb in product(ops, repeat=n)]

def calculate_result( numbers, operations ):
    if len(numbers) != len(operations) + 1:
        print("Operations too long or too short")

    result = numbers[0]
    currentOperation = 0

    for i in range(1, len(numbers)):
        if operations[currentOperation] == Operation.ADD:
            result += numbers[i]
        elif operations[currentOperation] == Operation.MUL:
            result *= numbers[i]
        else:
            result = int(str(result) + str(numbers[i]))
        currentOperation += 1

    return result

with open("2024/inputs/07.txt", "r") as f:

    lines = f.readlines()

    total_first = 0
    total_second = 0

    for line in lines:
        line = line.strip()
        if line == "":
            continue

        line = line.split(":")

        targetResult = int(line[0])
        nums = line[1].strip()
        nums = [int(num.strip()) for num in nums.split(" ")]

        operations_list = generate_permutations(len(nums) - 1)

        skip_second = False

        for operations in operations_list:
            #print(targetResult, nums, calculate_result(nums, operations))
            if targetResult == calculate_result(nums, operations):
                total_first += targetResult
                skip_second = True
                break

        if skip_second:
            continue

        operations_list = generate_permutations(len(nums) - 1, ops=[Operation.ADD, Operation.MUL, Operation.CON])

        for operations in operations_list:
            if targetResult == calculate_result(nums, operations):
                total_second += targetResult
                break
        
    print(f"First answer: {total_first}") 
    print(f"Second answer: {total_first + total_second}")
