import sys

def sorted_squares(sequence):
    startingIndex, startingNum = None, sys.maxsize
    for index, num in enumerate(sequence):
        if abs(num) < abs(startingNum):
            startingNum, startingIndex = num, index
    
    sol, lo, hi = [startingNum * startingNum], startingIndex - 1, startingIndex + 1
    while lo >= 0 or hi < len(sequence):
        if lo == -1:
            sol.append(sequence[hi] * sequence[hi])
            hi += 1
        elif hi == len(sequence):
            sol.append(sequence[lo] * sequence[lo])
            lo -= 1
        else:
            if abs(sequence[lo]) < abs(sequence[hi]):
                sol.append(sequence[lo] * sequence[lo])
                lo -= 1
            else:
                sol.append(sequence[hi] * sequence[hi])
                hi += 1
    return sol