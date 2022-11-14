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

def filter_seq_duplicates(lst: Node):
    curNode, prevNode = lst, None
    while curNode:
        if prevNode and prevNode.value == curNode.value:
            prevNode.next = curNode.next
        else:
            prevNode = curNode
        curNode = curNode.next

    return stringify_list(lst)
