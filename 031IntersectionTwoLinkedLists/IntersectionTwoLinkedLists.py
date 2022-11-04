class Node(object):
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

def list_length(lst):
    length = 0
    while lst != None:
        length += 1
        lst = lst.next
    
    return length

def find_lists_intersection(lstA, lstB):
    lengthA = list_length(lstA)
    lengthB = list_length(lstB)

    if lengthA > lengthB:
        for i in range(lengthA - lengthB):
            lstA = lstA.next
    else:
        for i in range(lengthB - lengthA):
            lstB = lstB.next

    while lstA != None and lstB != None:
        if lstA.value == lstB.value:
            return lstA.value

        lstA, lstB = lstA.next, lstB.next

    return None
