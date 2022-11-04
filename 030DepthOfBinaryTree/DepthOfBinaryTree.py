class Node(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

def get_binary_tree_depth(node):
    if node.left == None and node.right == None:
        return 1
    
    curSubtreeMaxDepth = 0
    for child in (node.left, node.right):
        if child == None:
            continue

        subtreeDepth = get_binary_tree_depth(child)
        if subtreeDepth > curSubtreeMaxDepth:
            curSubtreeMaxDepth = subtreeDepth
    
    return curSubtreeMaxDepth + 1
