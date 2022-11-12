def partition(nums, lo, hi):
    pivot = nums[hi]
    swapPointer = lo
    for i in range(lo, hi):
        if nums[i] <= pivot:
            nums[i], nums[swapPointer] = nums[swapPointer], nums[i]
            swapPointer += 1
    nums[hi], nums[swapPointer] = nums[swapPointer], nums[hi]
    return swapPointer

def quick_select(nums, k):
    k -= 1
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        pivotIndex = partition(nums, lo, hi)
        if k == pivotIndex:
            return nums[k]
        elif k < pivotIndex:
            hi = pivotIndex - 1
        elif k > pivotIndex:
            lo = pivotIndex + 1
    return -1
