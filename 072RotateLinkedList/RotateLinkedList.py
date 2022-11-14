class Node(object):
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

def stringify_list(lst):
    sol = ''
    while lst:
        sol += str(lst.value)
        lst = lst.next
    return sol

def rotate_list(lst, nOfRotations):
    lengthCtr, temp = 0, lst
    while temp:
        lengthCtr, temp = lengthCtr + 1, temp.next

    nOfRotations %= lengthCtr
    if nOfRotations == 0:
        return stringify_list(lst)

    curNode, newRoot = lst, None
    for elIndexDesc in range(lengthCtr - 1, -1, -1):
        if elIndexDesc - nOfRotations == 0: # new last node
            newRoot = curNode.next
            curNode.next, curNode = None, newRoot
        elif elIndexDesc == 0:    # last node, perform the rotation; last iteration - setting next node not important
            curNode.next = lst
        else:
            curNode = curNode.next
    return stringify_list(newRoot)
