class Node(object):
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

def serialize_bin_tree(tree):
    if tree == None:
        return "#"
    return str(tree.value) + serialize_bin_tree(tree.left) + serialize_bin_tree(tree.right)

def deserialize_bin_tree(tree):
    return deserialize_helper(tree, 0)[0]

def deserialize_helper(tree, leftIndex):
    if tree[leftIndex] == "#":
        return (None, leftIndex)

    newNode = Node(tree[leftIndex])
    newNode.left, rightIndex = deserialize_helper(tree, leftIndex + 1)
    newNode.right, curIndex = deserialize_helper(tree, rightIndex + 1)

    return (newNode, curIndex)
