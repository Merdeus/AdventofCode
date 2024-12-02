

def arereportssafe(reps : list[int]):

    is_unsafe = False
    is_inc = None
    previous_rep = reps[0]
    for i in range(1,len(reps)):
        
        diff = reps[i] - previous_rep

        if abs(diff) == 0 or abs(diff) > 3:
            is_unsafe = True
            break

        if is_inc is None:
            is_inc = diff > 0
        else:
            if (is_inc and diff < 0) or (not is_inc and diff > 0):
                is_unsafe = True
                break
        
        previous_rep = reps[i]

    return not is_unsafe

def getrepspermutations(reps : list[int]):
    results = []
    results.append(reps)

    for i in range(len(reps)):
        results.append(reps[:i] + reps[i+1:])

    return results

with open("2024/inputs/02.txt", "r") as f:

    total_first = 0
    total_second = 0

    for line in f:
        reps = line.split(" ")
        reps = [int(s) for s in reps]

        if arereportssafe(reps):
            total_first += 1

        reps_perm = getrepspermutations(reps)
        for reps in reps_perm:
            if arereportssafe(reps):
                total_second += 1
                break

    print(f"First answer: {total_first}")
    print(f"Second answer: {total_second}")