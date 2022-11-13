from collections import deque

class Node(object):
    def __init__(self, char, isWord = False, children = {}):
        self.letter = char
        self.isWord = isWord
        self.children = children

class Solution(object):
    def __init__(self, words):
        self.wordTrie = self.transform_to_trie(words)

    def build_word_subtree(self, parent, word, curIndex):
        doesNodeAlreadyExist, curLetter = word[curIndex] in parent.children, word[curIndex] # checking if the letter has already been inserted
        if curIndex + 1 == len(word):   # LAST LETTER
            if doesNodeAlreadyExist:
                parent.children[curLetter].isWord = True
            else:
                parent.children[curLetter] = Node(curLetter, True, {})
        else:
            if not doesNodeAlreadyExist:
                parent.children[curLetter] = Node(curLetter, False, {})
            self.build_word_subtree(parent.children[curLetter], word, curIndex + 1)
        return parent

    def transform_to_trie(self, words):
        root = Node(None, False, dict())
        for word in words:
            root = self.build_word_subtree(root, word, 0)
        return root

    def find_autocompletes(self, node, curPrefix, res):
        if node.isWord:
            res.append(curPrefix)
        if len(node.children) == 0:
            return res
        for letter in node.children:
            self.find_autocompletes(node.children[letter], curPrefix + letter, res)
        return res

    def autocomplete(self, prefix):
        curNode = self.wordTrie
        for letter in prefix:
            if letter not in curNode.children:
                return []
            curNode = curNode.children[letter]

        # at this point, curNode carries the node in the tree tied to the entire prefix
        return self.find_autocompletes(curNode, prefix, [])
