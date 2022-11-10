def circle_of_words(words):
    firstLetters, lastLetters = {}, {}
    for word in words:
        firstLetter, lastLetter = word[0], word[-1]
        if firstLetter not in firstLetters:
            firstLetters[firstLetter] = 0 
        firstLetters[firstLetter] += 1
        if lastLetter not in lastLetters:
            lastLetters[lastLetter] = 0 
        lastLetters[lastLetter] += 1
    
    for letter in firstLetters:
        if letter not in lastLetters or firstLetters[letter] != lastLetters[letter]:
            return False
    return True
