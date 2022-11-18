class Node(object):
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

def arithmetic(tree):
    if not tree.left and not tree.right:
        return tree.value
    return operations[tree.value](arithmetic(tree.left), arithmetic(tree.right))
