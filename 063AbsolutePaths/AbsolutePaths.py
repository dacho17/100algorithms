def simplify_path(path):
    stack = []
    for segment in path.split("/")[:-1]:
        if segment == '..':
            stack.pop()
        elif segment != '.':
            stack.append(segment)
    res = ''
    for segment in stack:
        res += segment + '/'
    return res
