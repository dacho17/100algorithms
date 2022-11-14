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

def swap_every_two_nodes(sequence):
    curNode = sequence
    while curNode and curNode.next:
        curNode.value, curNode.next.value = curNode.next.value, curNode.value
        curNode = curNode.next.next
    return stringify_list(sequence)
