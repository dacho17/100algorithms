from collections import defaultdict

# adding char +1 value into dictionary will mean that the character went out of the sliding window
# adding char -1 value into dictionary will mean that the value is now within the sliding window
# only target word chars are encoded with positive numbers and can be found in the sliding window from the beginning
# when sliding window dict is empty, this means that the sliding window currently contains only target word chars
# conceptually: non target word chars will represent excess in this window. Target word chars will represent lack in the window.
def find_anagrams(string, word):
    wordChars = defaultdict(int)
    for char in word:
        wordChars[char] += 1

    results = []
    for index, char in enumerate(string):
        if index >= len(word):
            leavingChar = string[index - len(word)]
            wordChars[leavingChar] += 1
            if wordChars[leavingChar] == 0:
                del wordChars[leavingChar]

        wordChars[char] -= 1
        if wordChars[char] == 0:
            del wordChars[char]

        if len(wordChars) == 0:
            results.append((index - len(word) + 1, index))
    return results
