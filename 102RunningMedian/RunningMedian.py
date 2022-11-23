import heapq

def add_to_heaps(value, maxHeap, minHeap, prevMedian):
    if value > prevMedian:
        heapq.heappush(minHeap, value)
    else:
        heapq.heappush(maxHeap, -value)

def rebalance_heaps(maxHeap, minHeap):
    if abs(len(maxHeap) - len(minHeap)) > 1:
        if len(maxHeap) > len(minHeap):
            highestSmaller = -heapq.heappop(maxHeap)
            heapq.heappush(minHeap, highestSmaller)
        else:
            smallestHigher = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -smallestHigher)

def get_median(maxHeap, minHeap):
    if len(maxHeap) == len(minHeap):
        return (-maxHeap[0] + minHeap[0]) / 2
    return -maxHeap[0] if len(maxHeap) > len(minHeap) else minHeap[0]


def get_sequence_medians(sequence):
    medians, maxHeap, minHeap, prevMedian = [], [], [], 0
    for value in sequence:
        add_to_heaps(value, maxHeap, minHeap, prevMedian)
        rebalance_heaps(maxHeap, minHeap)
        prevMedian = get_median(maxHeap, minHeap)
        medians.append(prevMedian)
    return medians
