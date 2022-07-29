class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def __str__(self):
        lst = "[ "
        node = self
        while node:
            lst += (str(node.val) + ", ")
            node = node.next
        lst += "]"
        return lst
    
def remove_from_end(node, k):
    # iterate through the list once and move 2 pointers
    slow, fast = node, node
    for i in range(k):
        fast = fast.next
    if not fast:
        return node.next
    fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return node
