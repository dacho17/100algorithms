class Magazine(object):
    def __init__(self, magazine):
        self.magazine = magazine
        
        self.array_length = ord('z') - ord('a') + 1
        self.index_offset = ord('a')
        
    def count_letters(self):
        self.array_of_letter_buckets = [0] * self.array_length

        for letter in self.magazine:
            index = ord(letter.lower()) - self.index_offset
            self.array_of_letter_buckets[index] += 1

    def can_be_spelled(self, word):
        if not word:
            return True

        self.count_letters()     # preprocess the magazine, count the letters

        for letter in word.lower():
            index = ord(letter) - self.index_offset
            
            if self.array_of_letter_buckets[index] == 0:
                return False
            
            self.array_of_letter_buckets[index] -= 1
        
        return True
