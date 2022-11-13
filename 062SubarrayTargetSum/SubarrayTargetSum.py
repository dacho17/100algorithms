def sliding_window(nums, target):   # my solution. only works with non-negative numbers
    first, curSum = 0, 0
    for index, num in enumerate(nums):
        curSum += num
        while curSum > target:
            curSum -= nums[first]
            first += 1
        if curSum == target:
            return nums[first: index + 1]
    return None

def subArraySum(nums, targetSum):   # solution which covers negative numbers also
    sums, curSum = {0: -1}, 0
    for index in range(0, len(nums)):
        curSum += nums[index]
        sums[curSum] = index
        if (curSum - targetSum) in sums:
            return nums[sums[curSum - targetSum] + 1: index + 1]
    return None
