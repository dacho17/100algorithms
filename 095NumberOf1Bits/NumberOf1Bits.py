def count_binary_ones(number):
    sol = 0
    while number > 0:
        sol += number & 1
        number = number >> 1
    return sol
