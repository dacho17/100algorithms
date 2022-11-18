from collections import defaultdict

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

def traverse_tree(tree, subtreeSums):
    if not tree.left and not tree.right:
        subtreeSums[tree.value] += 1
        return tree.value
    sumLeft = traverse_tree(tree.left, subtreeSums) if tree.left else 0
    sumRight = traverse_tree(tree.right, subtreeSums) if tree.right else 0
    totalSum = sumLeft + sumRight + tree.value
    subtreeSums[totalSum] += 1
    return totalSum 

def find_most_frequent_subtree_sum(tree):
    subtreeSums = defaultdict(int)
    traverse_tree(tree, subtreeSums)
    sumAmount, sumFreq = 0, 0
    for ss in subtreeSums:
        if subtreeSums[ss] > sumFreq:
            sumAmount, sumFreq = ss, subtreeSums[ss]
    return (sumAmount, sumFreq)
