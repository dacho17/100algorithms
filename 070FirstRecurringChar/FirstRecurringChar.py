def find_first_reocurring(seq):
    seen = set()
    for token in seq:
        if token in seen:
            return token
        seen.add(token)
    return None
