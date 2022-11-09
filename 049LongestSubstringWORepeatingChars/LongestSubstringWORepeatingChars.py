def get_length_of_unique_substring(sequence):
    charIndices, startIndex, maxLength = {}, -1, 0
    for index in range(0, len(sequence)):
        curChar = sequence[index]
        if curChar in charIndices and charIndices[curChar] > startIndex:
            startIndex = charIndices[curChar]
        charIndices[curChar] = index
        maxLength = max(maxLength, index - startIndex)

    return maxLength
