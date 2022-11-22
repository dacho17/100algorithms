class Node(object):
    def __init__(self, char, isWord=False, children=dict()):
        self.value = char
        self.isWord = isWord
        self.children = children

def create_trie_and_find_words(words):
    sortedWords = sorted(words, key=lambda word: len(word))
    root, concatenatedWords = Node(None, False, dict()), []
    for word in sortedWords:
        curNode, wordAdded = root, False
        for letterIndex in range(0, len(word)):
            if word[letterIndex] not in curNode.children:
                isFinalLetter = True if letterIndex == len(word) - 1 else False
                curNode.children[word[letterIndex]] = Node(word[letterIndex], isFinalLetter, dict())
            curNode = curNode.children[word[letterIndex]]
            if not wordAdded and curNode.isWord and letterIndex + 1 != len(word) and word[letterIndex + 1] in root.children:
                nodeAfterPrefix = root
                for sufixLetterIndex in range(letterIndex + 1, len(word)):
                    if word[sufixLetterIndex] not in nodeAfterPrefix.children:
                        break
                    nodeAfterPrefix = nodeAfterPrefix.children[word[sufixLetterIndex]]
                    if sufixLetterIndex + 1 == len(word) and nodeAfterPrefix.isWord:
                        concatenatedWords.append(word)
                        wordAdded = True
    return concatenatedWords

def get_concatenated_words(words):
    return create_trie_and_find_words(words)
