def unique_ways_req(m, n):
    if m == 1 or n == 1:
        return 1
    return unique_ways_req(m - 1, n) + unique_ways_req(m, n - 1)

def unique_ways_DP(m, n):
    matrix = {}
    for row in range(0, m):
        for col in range(0, n):
            if col == 0 or row == 0:
                matrix[(row, col)] = 1
            else:
                matrix[(row, col)] = matrix[(row - 1, col)] + matrix [(row, col - 1)]
    return matrix[(m - 1, n - 1)]
