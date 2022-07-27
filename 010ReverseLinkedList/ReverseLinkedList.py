class Node(object):
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

def reverse_list(root):
    new_root = reverse_list_internal(root)
    return to_list(new_root)

def reverse_list_internal(current, prev=None):
    next = current.next
    current.next = prev
    
    if next == None:
        return current
    return reverse_list_internal(next, current)

def to_list(lst):
    if not lst:
        return []
    res = to_list(lst.next)
    res.insert(0, lst.value)
    return res
