def longest_increasing_subsequence(sequence):
    subseqLengths = []
    for token in sequence:
        lengthConsidered = len(subseqLengths) - 1
        while lengthConsidered >= 0:
            if token > subseqLengths[lengthConsidered]:
                break
            lengthConsidered -= 1
        if lengthConsidered + 1 == len(subseqLengths):
           subseqLengths.append(token)
        else:
            subseqLengths[lengthConsidered + 1] = token
    return len(subseqLengths)
