def get_parentheses_comb(n):    
    return n_of_valid_parentheses_comb(n, 0)

def n_of_valid_parentheses_comb(parToOpen, parOpened):
    if parToOpen == 0 and parOpened == 0:
        return 1

    nOfValid = 0

    if parToOpen > 0:
        nOfValid += n_of_valid_parentheses_comb(parToOpen -1, parOpened + 1)
    if parOpened > 0:
        nOfValid += n_of_valid_parentheses_comb(parToOpen, parOpened - 1)

    return nOfValid
