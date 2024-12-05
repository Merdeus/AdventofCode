import math

update_rules = []
updates = []

# only checks if the current number is allowed not the preceding list itself
# this could be fancily done with recursive and faster
def precedingAllowed(pageNumber : int, preceding : list[int]) -> bool:
    if len(preceding) < 1:
        return True
    
    for num in preceding:
        for rule in update_rules:
            if pageNumber == rule[0] and num == rule[1]:
                return False
    return True

def getMiddleNumber(update : list[int]) -> int:
    return update[math.ceil(len(update)/2) - 1]

def orderUpdate(update : list[int]) -> list[int]:

    # this can be done more optimised but it works
    for m in range(len(update)):
        for i in range(len(update)):
            if not precedingAllowed(update[i], [update[j] for j in range(i)]):
                update[i], update[i-1] = update[i-1], update[i]

    return update

with open("2024/inputs/05.txt", "r") as f:

    lines = f.readlines()

    for line in lines:
        if line == "":
            continue
        elif line.count("|") > 0:
            rule = line.split("|")
            rule = [int(r.strip()) for r in rule]
            update_rules.append(rule)
        elif line.count(",") > 0:
            update = line.split(",")
            update = [int(r.strip()) for r in update]
            updates.append(update)

    correct_updates = []
    incorrect_updates = []

    for update in updates:
        current_preceding = []
        updateCorrect = True

        for num in update:
            if len(current_preceding) > 0:
                if not precedingAllowed(num, current_preceding):
                    updateCorrect = False
                    break
            current_preceding.append(num)
        
        if updateCorrect:
            correct_updates.append(update)
        else:
            incorrect_updates.append(update)

    total_first = 0
    total_second = 0

    for update in correct_updates:
        total_first += getMiddleNumber(update)

    print(f"First answer: {total_first}")

    for update in incorrect_updates:
        update = orderUpdate(update)
        total_second += getMiddleNumber(update)

    print(f"Second answer: {total_second}")