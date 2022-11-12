from collections import deque

class Node(object):
    def __init__(self, val, children = None):
        self.value = val
        self.children = children

def list_bfs(root):
    queue, res = deque(), []
    queue.append(root)
    while queue:
        curNode = queue.popleft()
        res.append(curNode.value)
        if curNode.children:
            [queue.append(child) for child in curNode.children]

    return res
