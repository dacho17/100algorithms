class Node(object):
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

# IN CASE COMPARISSONS ARE NOT ALLOWED: Traverse the first tree, find the node and remember the path.
# Traverse the same path in the second tree
def find_the_node(tree1, tree2, node):
    if not tree1:
        return None
    if tree1.value == node.value:
        return tree2.value
    return find_the_node(tree1.left, tree2.left, node) or find_the_node(tree1.right, tree2.right, node)
