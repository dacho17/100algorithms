operands = set(['-', '+', '/', '*'])
operations = {
    '-': lambda a, b: a - b,
    '+': lambda a, b: a + b,
    '/': lambda a, b: a / b,
    '*': lambda a, b: a * b
}

def calculate_reverse_polish_notation(sequence):
    stack = []
    for token in sequence:
        if token in operands:
            second, first = stack.pop(), stack.pop()
            res = operations[token](first, second)
            stack.append(res)
        else:
            stack.append(token)
    return stack[0]
