class Node(object):
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

def serialize_bin_tree(tree):
    if tree == None:
        return "#"
    return str(tree.value) + serialize_bin_tree(tree.left) + serialize_bin_tree(tree.right)

def prune_lower_than(tree, filterVal):
    if tree == None:
        return None

    tree.left = prune_lower_than(tree.left, filterVal)
    tree.right = prune_lower_than(tree.right, filterVal)
    
    if tree.value != filterVal and not tree.left and not tree.right:
        return None
    return tree
