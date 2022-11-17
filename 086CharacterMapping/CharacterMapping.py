def are_strings_bijective(str1, str2):
    if len(str1) != len(str2):
        return False
    
    mappings12, mappings21 = {}, {}
    for char1, char2 in zip(str1, str2):
        if char1 not in mappings12:
            mappings12[char1] = char2
        if char2 not in mappings21:
            mappings21[char2] = char1
        if mappings12[char1] != char2 or mappings21[char2] != char1:
            return False
    return True
