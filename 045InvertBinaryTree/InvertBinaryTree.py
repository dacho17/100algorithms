class Node(object):
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

    def __repr__(self):
        result = str(self.value)
        result += f"{self.left}" if self.left else ''
        result += f"{self.right}" if self.right else ''
        return result

def invert_binary_tree(tree):
    if tree == None or (tree.left == None and tree.right == None):
        return tree
    
    tree.right, tree.left = invert_binary_tree(tree.left), invert_binary_tree(tree.right)
    return tree
