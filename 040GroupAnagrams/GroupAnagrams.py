def group_anagrams(lstOfWords):
    anagramGroups = {}
    for word in lstOfWords:
        letterFrequency = 26 * [0]
        for letter in word:
            charIndex = ord(letter.lower()) - ord('a')
            letterFrequency[charIndex] += 1

        key = tuple(letterFrequency)
        if key not in anagramGroups:
            anagramGroups[key] = []
        anagramGroups[key].append(word)

    return list(anagramGroups.values())
