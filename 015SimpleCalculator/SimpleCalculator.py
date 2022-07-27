from operator import eq


def calculate(equation, index=0, multiplicator=1):
    sum = 0
    while index < len(equation):
        token = equation[index]
        if  token == "+":
            multiplicator = 1
        elif token == "-":
            multiplicator = -1
        elif token.isdigit():
            sum += (multiplicator * int(equation[index]))
        elif token == "(":
            exp_ev, index = calculate(equation, index + 1, 1)
            sum += (multiplicator * exp_ev)
        elif token == ")":
            return sum, index
        index += 1
    return sum
