def get_max_sum(lst):
    maxSum, curSum = 0, 0
    for num in lst:
        curSum = curSum + num if curSum + num > 0 else 0
        maxSum = max(maxSum, curSum)
    return maxSum
