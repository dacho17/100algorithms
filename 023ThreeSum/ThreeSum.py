def three_sum_brute(nums):
    res = []
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append((nums[i], nums[j], nums[k]))
    return res

def three_sum_hash(nums):
    res = []
    for target in range(0, len(nums)):      # iterate n times (through target sums)
        stored_addends = {}
        for i in range(target + 1, len(nums)):
            if -nums[target] - nums[i] in stored_addends:     # a + b + c = 0 -> nums[i] + sored_addend[x] = -target
                res.append((nums[i], -nums[target] - nums[i], nums[target]))
            stored_addends[nums[i]] = 1
    return res

def three_sum_pointers(nums):
    nums.sort()
    res = []
    for target in range(0, len(nums)):      # iterate n times (through target sums)
        low = target + 1
        high = len(nums) - 1
        while high > low:
            three_sum = nums[target] + nums[low] + nums[high]
            if three_sum == 0:
                res.append((nums[target], nums[low], nums[high]))
                high -= 1   # or low += 1
            elif three_sum > 0:
                high -= 1
            elif three_sum < 0:
                low += 1
    return res
