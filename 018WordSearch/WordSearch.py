class WordGrid(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def find(self, word):
        for row in range(0, len(self.matrix)):
            letter_ptr = 0
            for col in range(0, len(self.matrix)):
                if self.matrix[row][col] == word[letter_ptr]:
                    letter_ptr += 1
                elif self.matrix[row][col] == word[0]:
                    letter_ptr = 1
                else:
                    letter_ptr = 0
                
                if letter_ptr == len(word):
                    return True
                 # heuristic to give up searching the row/column if the number of elements remaining is not enough to finish the word
                if len(word) - letter_ptr > len(self.matrix) - col - 1:
                    break
        
        for col in range(0 , len(self.matrix)):
            letter_ptr = 0
            for row in range(0, len(self.matrix)):
                if self.matrix[row][col] == word[letter_ptr]:
                    letter_ptr += 1
                elif self.matrix[row][col] == word[0]:
                    letter_ptr = 1
                else:
                    letter_ptr = 0
                
                if letter_ptr == len(word):
                    return True
                 # heuristic to give up searching the row/column if the number of elements remaining is not enough to finish the word
                if len(word) - letter_ptr > len(self.matrix) - row - 1:
                    break

        return False
