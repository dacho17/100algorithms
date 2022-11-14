# Rules:
# . cannot appear:
#   after it has already been seen, or
#   after e
# - cannot appear:
#   on non-first index
# e cannot appear:
#   twice, and
#   must be followed by a digit

# NOTE: This solution can be made more robust, and most likely does not cover all the cases
def is_valid_number(sequence):
    dotSeen, eSeen, eValid, digitSeen = False, False, True, False
    for index, token in enumerate(sequence):
        if token == '.':
            if dotSeen or eSeen:
                return False
            dotSeen = True
        elif token == '-':
            if index != 0:
                return False
        elif token == 'e':
            if eSeen:
                return False
            eSeen, eValid = True, False
        elif token in set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
            if eSeen:   # can go without this comparison also
                eValid = True
            digitSeen = True
        else:
            return False
    return True and digitSeen and eValid
