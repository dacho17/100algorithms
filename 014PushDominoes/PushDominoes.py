import sys

def _get_equilibrium(lst):
    res = [0] * len(lst)
    
    curr_force = 0
    for i in range(0, len(lst)):            # Summing up forces acting right (R)
        if lst[i] == "R":                   # force is created
            curr_force = sys.maxsize
        elif lst[i] == "L":                 # opposite force is created, so R force stops influencing further environment
            curr_force = 0
        res[i] += curr_force
        if curr_force > 0:                  # if the force influence exists, it decreases going further
            curr_force -= 1

    curr_force = 0
    for i in range(len(lst) - 1, -1, -1):   # Summing up forces acting left (L)
        if lst[i] == "R":                   # opposite force is created, so L force stops influencing further environment
            curr_force = 0
        elif lst[i] == "L":                 # force is created
            curr_force = -sys.maxsize            
        res[i] += curr_force
        if curr_force < 0:                  # if the force influence exists, it decreases going further
            curr_force += 1

    final_res = transform_to_LR(res)
    return final_res

def transform_to_LR(lst):
    res = ""
    for force in lst:
        if force > 0:
            res += "R"
        elif force < 0:
            res += "L"
        else:
            res += "."
    return res
