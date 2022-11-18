def partition(sequence, k):
    cur, lo, hi,  = 0, 0, len(sequence) - 1
    while cur <= hi:
        if sequence[cur] > k:
            sequence[cur], sequence[hi] = sequence[hi], sequence[cur]
            hi -= 1
        elif sequence[cur] < k:
            sequence[cur], sequence[lo] = sequence[lo], sequence[cur]
            lo += 1
            cur += 1
        else:   # sequence[cur] == k:
            cur += 1
    return sequence
