def merge_intervals(intervals):
    intervals = sorted(intervals, key=lambda interval : (interval[0]))

    sol = []
    currentStart, currentEnd = intervals[0]
    for index in range (1, len(intervals)):
        if currentStart <= intervals[index][0] <= currentEnd:
            currentEnd = max(currentEnd, intervals[index][1])
        else:
           sol.append((currentStart, currentEnd))
           currentStart, currentEnd = intervals[index]

    if len(sol) == 0 or sol[-1] != (currentStart, currentEnd):
        sol.append((currentStart, currentEnd))

    return sol
