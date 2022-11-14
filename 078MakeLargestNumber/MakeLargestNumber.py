from functools import cmp_to_key

def build_largest_number(sequence):
    customSorted = sorted(sequence, key=cmp_to_key(
        lambda a, b:
            1 if str(a) + str(b) < str(b) + str(a) else -1
    ))
    res = ''.join(str(num) for num in customSorted)
    return res
