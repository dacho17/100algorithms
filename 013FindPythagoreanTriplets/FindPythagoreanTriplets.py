def any_pythagorean_triplets(lst):
    squared = set([i * i for i in lst])
    
    for i in squared:
        for j in squared:
            if i != j and i + j in squared:
                return True
    return False