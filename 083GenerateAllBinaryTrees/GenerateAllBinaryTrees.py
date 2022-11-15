def generate_all_binary_trees(number):
    return generate_all_binary_trees_helper([n for n in range(1, number + 1)])

def generate_all_binary_trees_helper(sequence):
    if len(sequence) <= 1:
        return [[sequence[0]]] if len(sequence) == 1 else [[]]
    
    resTreeCombinations = []
    for index in range(0, len(sequence)):
        curValue = [sequence[index]]
        leftTrees = generate_all_binary_trees_helper(sequence[0:index])
        rightTrees = generate_all_binary_trees_helper(sequence[index + 1: len(sequence)])
        for lTree in leftTrees:
            for rTree in rightTrees:
                resTreeCombinations.append(lTree + curValue + rTree)
    return resTreeCombinations
