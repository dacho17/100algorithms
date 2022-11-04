def find_first_missing_positive(lst):
    positivesExpected = len(lst)

    positives = set()
    for num in lst:
        if (num > 0):
            positives.add(num)
    
    for expected in range(1, positivesExpected + 1):
        if expected not in positives:
            return expected
    
    return None
