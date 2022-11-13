def longest_range_of_ones(decNum):
    longest, currOnes = 0, 0
    while decNum > 0:
        currOnes = currOnes + 1 if decNum & 1 else 0
        decNum = decNum >> 1    # shifting right
        longest = max(longest, currOnes)
    return max(longest, currOnes)
