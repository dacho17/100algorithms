def constant_find_non_duplicate(numbers):
    res = 0
    for number in numbers:
        res ^= number
    return res

def linear_find_non_duplicate(numbers):
    hash_map = {}

    for number in numbers:
        if number not in hash_map:
            hash_map[number] = 0
        hash_map[number] += 1
    
    for number, ocurrence in hash_map.items():
        if ocurrence == 1:
            return number
