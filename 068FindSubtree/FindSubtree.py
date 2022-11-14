class Node(object):
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

def find_subtree(tree: Node, subtree: Node) -> bool:
    if not tree or not subtree:
        return not tree and not subtree

    isMatch = tree.value == subtree.value \
        and (find_subtree(tree.left, subtree.left)) \
        and (find_subtree(tree.right, subtree.right))
    return True if isMatch else \
        find_subtree(tree.left, subtree) or find_subtree(tree.right, subtree)
