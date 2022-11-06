class Node(object):
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

def get_nodes(tree, targetHeight, curHeight = 1):
    if curHeight == targetHeight:
        return [tree.value]

    res = []
    if tree.left != None:
        res.extend(get_nodes(tree.left, targetHeight, curHeight + 1))
    if tree.right != None:
        res.extend(get_nodes(tree.right, targetHeight, curHeight + 1))

    return res

def get_elements_at_height(tree, targetHeight):
    return get_nodes(tree, targetHeight)
