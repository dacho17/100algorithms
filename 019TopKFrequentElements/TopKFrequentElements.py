import heapq

def get_top_k_frequent(nums, k):
    count = {}
    for num in nums:
        if num not in count:    # Python allows initializing default dicitonary: count = collections.defaultdict(int)
            count[num] = 0
        count[num] += 1
    
    heap = []
    for num, c in count.items():
      heap.append((-c, num))    # default heap in Python is min heap (max heap is needed & that is why - is used)
    heapq.heapify(heap)
    
    maxes = []
    for i in range(k):
        maxes.append(heapq.heappop(heap)[1])
    return maxes
