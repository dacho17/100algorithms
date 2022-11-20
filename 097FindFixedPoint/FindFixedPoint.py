def find_fixed_point(sequence):
    lo, hi = 0, len(sequence) - 1
    while lo < hi:
        cur = (hi + lo) // 2
        if sequence[cur] > cur:
            hi = cur - 1
        elif sequence[cur] < cur:
            lo = cur + 1
        else:
            return cur
    cur = (hi + lo) // 2
    return cur if sequence[cur] == cur else None
