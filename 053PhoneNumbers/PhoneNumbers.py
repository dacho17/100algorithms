
                
def encode_valid_words():
    validWords = ['cat', 'dog', 'mat', 'atm', 'bed', 'but', 'tub', 'bar', 'cab', 'caf', 'cad', 'car']
    validCombinations = {}
    for word in validWords:
        encodedWord = ''
        for letter in word:
            if letter in ('a', 'b', 'c'):
                encodedWord += '2'
            if letter in ('d', 'e', 'f'):
                encodedWord += '3'
            if letter in ('g', 'h', 'i'):
                encodedWord += '4'
            if letter in ('j', 'k', 'l'):
                encodedWord += '5'
            if letter in ('m', 'n', 'o'):
                encodedWord += '6'
            if letter in ('p', 'q', 'r', 's'):
                encodedWord += '7'
            if letter in ('t', 'u', 'v'):
                encodedWord += '8'
            if letter in ('w', 'x', 'y', 'z'):
                encodedWord += '9'
    
        if encodedWord not in validCombinations:
            validCombinations[encodedWord] = []
        validCombinations[encodedWord].append(word)
    return validCombinations

def generate_words_from(number):
    validWords = encode_valid_words()
    return validWords[number] if number in validWords else []
