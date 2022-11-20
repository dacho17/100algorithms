class Node(object):
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

def get_target_depth(tree, targetNode, curDepth):
    if tree == None:
        return -1
    if tree.value == targetNode.value:
        return curDepth
    return max(get_target_depth(tree.left, targetNode, curDepth + 1), get_target_depth(tree.right, targetNode, curDepth + 1))

def get_nodes_at_depth(tree, targetDepth, curDepth):
    if tree == None:
        return []
    if targetDepth == curDepth:
        return [tree.value]
    return get_nodes_at_depth(tree.left, targetDepth, curDepth + 1) + get_nodes_at_depth(tree.right, targetDepth, curDepth + 1)

def find_cousins(tree, targetNode):
    targetDepth = get_target_depth(tree, targetNode, 1)
    return get_nodes_at_depth(tree, targetDepth, 1)
