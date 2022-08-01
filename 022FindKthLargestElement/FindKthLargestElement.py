import heapq
import random

def findKthLargestSort(nums, k):
    return sorted(nums)[-k]

def findKthLargestHeap(nums, k):
    return heapq.nlargest(k, nums)[-1]

def findKthLargestQuickSelect(nums, k):
    def select(lst, l, r, k_index):
        if l == r:
            return lst[l]
        pivot_index = (l + r) // 2
        print(nums, l, r, pivot_index)
        lst[l], lst[pivot_index] = lst[pivot_index], lst[l] # move pivot to the beginning of the list

        i = l
        for j in range(l + 1, r + 1):
            if lst[j] < lst[l]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        
        lst[i], lst[l] = lst[l], lst[i] # move pivot to the correct location
        if k_index == len(nums) - i:
            return lst[i]
        elif k_index > len(nums) - i:
            return select(lst, l, i - 1, k_index)
        else:
            return select(lst, i + 1, r, k_index)

    return select(nums, 0, len(nums) - 1, k)

def findKthLargestQuickSelectYT(nums, k):
    def select(lst, l, r, k_index):
        pivot_index = r

        print(lst)
        i = l - 1
        for j in range(l, r + 1):
            if lst[j] <= lst[pivot_index] or j == r:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        print(lst)

        # lst[i + 1], lst[pivot_index] = lst[pivot_index], lst[i + 1] # move pivot to the correct location
        if k_index == len(lst) - i:
            return lst[i]
        elif k_index > len(lst) - i:
            return select(lst, l, i - 1, k_index)
        else:
            return select(lst, i + 1, r, k_index)

    return select(nums, 0, len(nums) - 1, k)
