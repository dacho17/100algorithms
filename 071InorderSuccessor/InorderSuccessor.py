class Node(object):
    def __init__(self, val, left=None, right=None, parent=None):
        self.value = val
        self.left = left
        self.right = right
        self.parent = parent

# NOTE: my solution, does not recognize successors who are larger by more than 1 from the given node value
# def find_successor_helper(curNode, priorNode, targetVal):
#     if not curNode:
#         return None
#     if curNode.value == targetVal:
#         return curNode

#     childNodeToVisit = curNode.left if targetVal < curNode.value else curNode.right
#     nodeToVisit = childNodeToVisit if priorNode == curNode.parent else curNode.parent
#     if not priorNode:
#         return find_successor_helper(curNode.parent, curNode, targetVal) or find_successor_helper(childNodeToVisit, curNode, targetVal)
#     else:
#         return find_successor_helper(nodeToVisit, curNode, targetVal)

# def find_successor(startNode: Node):
#     return find_successor_helper(startNode, None, startNode.value + 1)


# NOTE: more efficient and elegant solution which better utilizes the properties of binary search tree
def find_successor(startNode: Node):
    if startNode.right:
        resNode = startNode.right
        while resNode.left:
            resNode = resNode.left
        return resNode
    
    current = startNode
    while current != current.parent.left: # current.value < current.parent.value ; NOTE: some parents do not have a value
        current = current.parent
    return current.parent
