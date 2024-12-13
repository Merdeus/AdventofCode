def solve(var, i, j, cset = None):

    possibleCombinations = set([])

    if cset is not None:
        for c in cset:
            (current_i, current_j) = c
            calc = current_i * i + current_j * j
            if calc == var:
                possibleCombinations.add((current_i,current_j))

    else:
        current_i = var // i
        current_j = 0

        while current_j < ((var // j) + 1):

            calc = current_i * i + current_j * j
            if calc == var:
                possibleCombinations.add((current_i,current_j))
                current_j += 1
                continue

            if calc > var:
                current_i -= 1
            else:
                current_j += 1
            
    return possibleCombinations

# the more boring and mathy way (and quicker)
# also only gives back one solution, luckily there is always only one.
def alternativeSolve(prize_x, prize_y, a_x, b_x, a_y, b_y):
    return (int((prize_x*b_y - prize_y*b_x) / (a_x*b_y - a_y*b_x)), int((a_x*prize_y - a_y*prize_x) / (a_x*b_y - a_y*b_x)))


def calcTokens(a,b):
    return 3*a + b

with open("2024/inputs/13.txt", "r") as f:

    data = f.read()
    data = data.split("\n\n")

    total_first = 0
    total_second = 0

    for t in data:
        tmp = []
        tm = t.split("\n")

        button_a = tm[0]
        button_a_x = int(button_a.split("X+")[1].split(",")[0])
        button_a_y = int(button_a.split("Y+")[1])

        button_b = tm[1]
        button_b_x = int(button_b.split("X+")[1].split(",")[0])
        button_b_y = int(button_b.split("Y+")[1])

        prize = tm[2]
        prize_x = int(prize.split("X=")[1].split(",")[0])
        prize_y = int(prize.split("Y=")[1])

        (sec_a,sec_b) = alternativeSolve(prize_x+10000000000000, prize_y+10000000000000, button_a_x, button_b_x, button_a_y, button_b_y)
        if sec_a > 0 and sec_b > 0:
            # not entirely sure why I have to check that the result is actually correct
            if (sec_a * button_a_x + sec_b * button_b_x) == prize_x+10000000000000:
                if (sec_a * button_a_y + sec_b * button_b_y) == prize_y+10000000000000:
                    total_second += calcTokens(sec_a, sec_b)

        # kept my original solve function for part 1 in, because it works and shows it can
        # be done differently besides cramers rule. But for part2 it is not feasible
        solutions = solve(prize_x, button_a_x, button_b_x)
        solutions = solve(prize_y, button_a_y, button_b_y, solutions)

        if len(solutions) < 1:
            continue

        currentLowest = None
        for solution in solutions:
            if currentLowest is None:
                currentLowest = solution
                continue

            (ca,cb) = currentLowest
            (sa,sb) = solution

            if calcTokens(sa,sb) < calcTokens(ca,cb):
                currentLowest = solution

        total_first += calcTokens(ca,cb)

    print(f"First answer: {total_first}")
    print(f"Second answer: {total_second}")

