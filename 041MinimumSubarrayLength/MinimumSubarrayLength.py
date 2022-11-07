def find_min_subarray_that_sums_to(targetSum, lst):
    startPtr, curSum = 0, 0
    minElements = targetSum + 1
    for curIndex in range(0, len(lst)):
        curSum += lst[curIndex]
        
        if curSum > targetSum:
            while curSum > targetSum:
                curSum -= lst[startPtr]
                startPtr += 1
        if curSum == targetSum:
            minElements = min(minElements, curIndex - startPtr + 1)        

    return minElements
