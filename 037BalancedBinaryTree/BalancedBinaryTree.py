class Node(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def is_tree_height_balanced(tree):
    if tree.left == None and tree.right == None:
        return (1, True)
    
    leftSubtreeHeight, isLeftBalanced = (0, True) if tree.left == None else is_tree_height_balanced(tree.left)
    rightSubtreeHeight, isRightBalanced = (0, True) if tree.right == None else is_tree_height_balanced(tree.right)

    isSubtreeBalanced = isLeftBalanced and isRightBalanced and abs(leftSubtreeHeight - rightSubtreeHeight) <= 1

    return (max(leftSubtreeHeight, rightSubtreeHeight) + 1, isSubtreeBalanced)
