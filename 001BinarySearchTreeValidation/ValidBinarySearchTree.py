class Node(object):
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node


def is_valid(node, low_threshold=None, high_threshold=None):
    if (not node):
        return True
    if (low_threshold and low_threshold > node.value):
        return False
    if (high_threshold and high_threshold < node.value):
        return False
    
    return is_valid(node.left_node, low_threshold, node.value) and is_valid(node.right_node, node.value, high_threshold)
