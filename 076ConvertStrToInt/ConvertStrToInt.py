def convert_str_to_int(strNum):
    sol, (startIndex, multiplicator) = 0, (1, -1) if strNum[0] == '-' else (0, 1)
    for index in range(startIndex, len(strNum)):
        sol = sol * 10 + ord(strNum[index]) - ord('0')
    return sol * multiplicator
