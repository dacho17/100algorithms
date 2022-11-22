class Node(object):
    def __init__(self, char, timesTraveled=0, children=dict()):
        self.value = char
        self.timesTraveled = timesTraveled
        self.children = children

def create_trie(words):
    root = Node(None, 0, dict())
    for word in words:
        curNode = root
        root.timesTraveled += 1
        for letter in word:
            if letter not in curNode.children:
                curNode.children[letter] = Node(letter, 0, dict())
            curNode = curNode.children[letter]
            curNode.timesTraveled += 1
    return root

def shortest_unique_prefix(words):
    trie, sol = create_trie(words), []
    for word in words:
        cur, letterIndex = trie, -1
        while letterIndex + 1 < len(word) and word[letterIndex + 1] in cur.children:
            letterIndex += 1
            cur = cur.children[word[letterIndex]]
            if cur.timesTraveled == 1:
                break
        sol.append(word[0: letterIndex + 1])
    return sol
