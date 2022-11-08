def find_array_intersection(lstA, lstB):    # aElements can also be the res, and then elements not appearing in lstB can be removed from res
    aElements = set(lstA)
    res = set()
    [res.add(element) for element in lstB if element in aElements]
    return res
