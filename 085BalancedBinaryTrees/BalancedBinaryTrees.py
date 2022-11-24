class Node(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

def is_tree_height_balanced(node):
    if not node.left and not node.right:
        return (True, 1)
    
    leftTree = (True, 0) if not node.left else is_tree_height_balanced(node.left)
    rightTree = (True, 0) if not node.right else is_tree_height_balanced(node.right)
    isBalanced = leftTree[0] and rightTree[0] and abs(leftTree[1] - rightTree[1]) <= 1

    return (isBalanced, max(leftTree[1], rightTree[1]) + 1)
