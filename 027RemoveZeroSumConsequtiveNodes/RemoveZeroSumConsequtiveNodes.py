class Node(object):
    def __init__(self, val, next=None):
        self.value = val
        self.next = next
    
    def __repr__(self):
        node = self
        ret = ''
        while node:
            ret += str(node.value) + ' '
            node = node.next
        return ret

def remove_zero_sum_conseq(root):
    temp_sum = 0
    active_sums_repo, active_sums_stack = {}, []

    cur = Node(0, root) # adding a dummy root
    while cur:
        temp_sum += cur.value
        if temp_sum not in active_sums_repo:
            active_sums_repo[temp_sum] = cur
        else:
            while True:
                prev_sum = active_sums_stack.pop()
                if prev_sum == temp_sum:
                    prev_node = active_sums_repo[temp_sum]
                    prev_node.next = cur.next
                    break
                del active_sums_repo[prev_sum]
        active_sums_stack.append(temp_sum)
        cur = cur.next

    return active_sums_repo[0].next # return first node after created dummy root
