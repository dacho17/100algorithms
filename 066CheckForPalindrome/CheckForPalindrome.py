from collections import defaultdict

def check_for_palindrome(seq):
    tokenCounter = defaultdict(int)
    for token in seq:
        tokenCounter[token] += 1

    sol = ''
    oddToken = None
    for token in tokenCounter:
        if tokenCounter[token] % 2 == 1:
            if oddToken:    # this would mean second odd token -> no palindrom
                return None
            oddToken = token
        else:
            sol += (token * (tokenCounter[token] // 2))
    return sol + (oddToken if oddToken else '') + sol[::-1]
