def calculate_time(jobSequence, cooldown):
    jobDict, curTime = dict(), 0
    for job in jobSequence:
        if job in jobDict:
            curTime = max(curTime, jobDict[job] + cooldown)
        curTime += 1
        jobDict[job] = curTime  # stores the time when the job has ended running
    return curTime
