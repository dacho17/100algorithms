guide = {
    "I": (1, 1),
    "V": (5, 1),
    "X": (10, 2),
    "L": (50, 2),
    "C": (100, 3),
    "D": (500, 3),
    "M": (1000, 4)
}

def transform_roman_dec(roman):
    curOrder, sol = 0, 0
    for i in range(len(roman) - 1, -1, -1):
        value, order = guide[roman[i]]
        sol += -value if order < curOrder else value
        curOrder = max(order, curOrder)
    return sol
