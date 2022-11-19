def binary_search_matrix(matrix, target):
    rowAmount, colAmount = len(matrix), len(matrix[0])
    lo, hi = 0, rowAmount * colAmount - 1
    while lo < hi:
        curIndex = (hi + lo) // 2
        checkElement = matrix[curIndex // colAmount][curIndex % colAmount]
        if checkElement == target:
            return True
        elif checkElement > target:
            hi = curIndex - 1
        elif checkElement < target:
            lo = curIndex + 1
    return matrix[((hi + lo) // 2) // colAmount][((hi + lo) // 2) % colAmount] == target
