import heapq

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

def merge_K_linked_lists(kLists):
    heap = []
    for lst in kLists:
        heap.append((lst.value, lst.next))
    heapq.heapify(heap)

    sol = None
    lastAdded = None
    while len(heap) != 0:
        minNode = heapq.heappop(heap)
        
        nodeToAdd = Node(minNode[0], None)
        if sol == None:
            sol = nodeToAdd
        else:
            lastAdded.next = nodeToAdd
        lastAdded = nodeToAdd

        if (minNode[1] != None):
            heapq.heappush(heap, (minNode[1].value, minNode[1].next))

    return sol
