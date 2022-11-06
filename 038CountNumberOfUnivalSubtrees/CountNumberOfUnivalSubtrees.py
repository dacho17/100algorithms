class Node(object):
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

def count_unival_subtrees(tree):
    if tree.left == None and tree.right == None:
        return (tree.value, True, 1)
    
    leftSubtreeVal, isLeftSubtreeUnival, cntL = (tree.value, True, 0) if tree.left == None else count_unival_subtrees(tree.left)
    rightSubtreeVal, isRightSubtreeUnival, cntR = (tree.value, True, 0) if tree.right == None else count_unival_subtrees(tree.right)

    cntThis = 1 if isLeftSubtreeUnival and isRightSubtreeUnival and (leftSubtreeVal == rightSubtreeVal == tree.value) else 0
    return (tree.value, cntThis, cntL + cntR + cntThis)
