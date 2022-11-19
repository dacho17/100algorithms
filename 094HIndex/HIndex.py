def determine_h_index(paperReferencesLst):
    nOfPapers = len(paperReferencesLst)
    scoreFreq = [0] * (nOfPapers + 1)
    for paperReferences in paperReferencesLst:
        markReferencesAs = nOfPapers if paperReferences > nOfPapers else paperReferences
        scoreFreq[markReferencesAs] += 1
    paperCounter = 0
    for potentialHIndex in range(nOfPapers, -1, -1):
        paperCounter += scoreFreq[potentialHIndex]
        if paperCounter >= potentialHIndex:
            return potentialHIndex
    return 0
