class MaxStack(object):
    def __init__(self):
        self.stack = []
        self.maxes = []

    def push(self, el):
        self.stack.append(el)

        if self.maxes and self.maxes[-1] > el:
            self.maxes.append(self.maxes[-1])
        else:
            self.maxes.append(el)

    def pop(self):
        self.maxes.pop()
        return self.stack.pop()

    def max(self):
        return self.maxes[-1]
