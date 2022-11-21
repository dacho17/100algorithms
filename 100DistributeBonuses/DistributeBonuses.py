def distribute_bonuses(performances):
    bonuses = [1] * len(performances)

    for performanceIndex in range(1, len(performances)):
        if performances[performanceIndex - 1] < performances[performanceIndex]:
            bonuses[performanceIndex] = bonuses[performanceIndex - 1] + 1
    
    for performanceIndex in range(len(performances) - 2, -1, -1):
        if performances[performanceIndex + 1] < performances[performanceIndex]:
            bonuses[performanceIndex] = max(bonuses[performanceIndex + 1] + 1, bonuses[performanceIndex])
    
    return bonuses
