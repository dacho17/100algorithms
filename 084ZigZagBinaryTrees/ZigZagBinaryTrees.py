class Node(object):
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

def zig_zag_binary_tree(node):
    sol, lrStack, rlStack = [], [node], []

    while len(lrStack) > 0 or len(rlStack) > 0:
        while len(lrStack) > 0:
            curNode = lrStack.pop()
            sol.append(curNode.value)
            if curNode.right:
                rlStack.append(curNode.right)
            if curNode.left:
                rlStack.append(curNode.left)
        while len(rlStack) > 0:
            curNode = rlStack.pop()
            if curNode.left:
                lrStack.append(curNode.left)
            if curNode.right:
                lrStack.append(curNode.right)
            sol.append(curNode.value)
    return sol
