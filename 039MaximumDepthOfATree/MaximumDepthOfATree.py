# Note - Recursion won't work on large trees, due to the limit on stack limit size.
# Iteration, on the other hand, uses heap space which is limited only by how
# much memory is in the computer.

class Node(object):
    def __init__(self, right=None, left=None):
        self.right = right
        self.left = left

def find_tree_depth(tree):
    maxDepth = 0
    stack = [(tree, 1)]

    while stack:
        (node, depth) = stack.pop()
        maxDepth = max(depth, maxDepth)
        
        if node.right != None:
            stack.append((node.right, depth + 1))
        if node.left != None:
            stack.append((node.left, depth + 1))
    return maxDepth
