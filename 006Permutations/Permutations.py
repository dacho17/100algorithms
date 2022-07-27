class ListForPermutation(object):
    def __init__(self, lst):
        self.lst = lst
        self.length = len(lst)
        self.permutations = []

    def return_permutations(self):
        self.permute()
        return self.permutations
        
    def permute(self, capo=0):      # capo is a swap_index
        for i in range(capo, self.length):
            if (capo == self.length - 1):
                self.permutations.append(list(self.lst))
            self.lst[i], self.lst[capo] = self.lst[capo], self.lst[i]
            self.permute(capo + 1)
            self.lst[i], self.lst[capo] = self.lst[capo], self.lst[i]
