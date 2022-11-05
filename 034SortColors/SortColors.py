def sort_colors(colors):    # colors are given as 0, 1, 2
    begPtr = 0
    endPtr = len(colors) - 1
    cur = 0

    while cur <= endPtr:
        if colors[cur] == 0:
            colors[begPtr], colors[cur] = colors[cur], colors[begPtr]
            begPtr += 1
            cur += 1
        elif colors[cur] == 1:
            cur += 1
        elif colors[cur] == 2:
            colors[endPtr], colors[cur] = colors[cur], colors[endPtr]
            endPtr -= 1
    
    return colors
