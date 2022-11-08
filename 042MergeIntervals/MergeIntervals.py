def get_intervals_from(lst):
    if not lst:
        return []
    
    sol, begnEl, endEl = [], lst[0], lst[0]
    for index in range(0, len(lst)):
        if lst[index] not in (endEl, endEl + 1):
            sol.append((begnEl, endEl))
            begnEl = lst[index]
        endEl = lst[index]

    sol.append((begnEl, endEl)) # appending the last range
    return sol
