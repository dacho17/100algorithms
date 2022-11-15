def as_sum_of_squares(number: int):
    addends, curAddend = [1], 2
    while curAddend * curAddend <= number:
        if curAddend * curAddend == number:
            return 1    # determine at once that the number can be a sum of one squared number
        addends.append(curAddend * curAddend)
        curAddend += 1
    
    stepsToReachNumbers = [num for num in range(0, number + 1)] # initializes the array which will be used in algorithm
    for curNum in range(0, number):
        for addend in addends:
            targetNumber = curNum + addend
            if targetNumber > number:
                break
            stepsToReachNumbers[targetNumber] = min(stepsToReachNumbers[curNum] + 1, stepsToReachNumbers[targetNumber])
    return stepsToReachNumbers[-1]
