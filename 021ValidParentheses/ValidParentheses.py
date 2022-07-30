def validate_parentheses(exp):
    stack, opening = [], set("([{")
    for par in exp:
        if par in opening:
            stack.append(par)
        elif not stack:     # if a closing parentheses is being read, there must be at least one opened parentheses
            return False
        elif par == ")" and stack[-1] == "(":
            stack.pop()
        elif par == "]" and stack[-1] == "[":
            stack.pop()
        elif par == "}" and stack[-1] == "{":
            stack.pop()
        else:
            return False
    return len(stack) == 0
