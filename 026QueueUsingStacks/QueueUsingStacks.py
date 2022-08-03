class StackyQueue(object):
    def __init__(self):
        self.pushy = []
        self.poppy = []

    def enqueue(self, el):
        while self.poppy:
            self.pushy.append(self.poppy.pop())
        self.pushy.append(el)

    def de_queue(self):
        if not self.poppy and not self.pushy:
            return None
        while self.pushy:
            self.poppy.append(self.pushy.pop())
        return self.poppy.pop()

## These are the done tests for this task! - All Passed
########################################
q = StackyQueue()
z = q.de_queue()
print(z)
q.enqueue(1)
print(q.pushy, q.poppy)
q.enqueue(2)
print(q.pushy, q.poppy)
q.enqueue(3)
print(q.pushy, q.poppy)
first = q.de_queue()
print(q.pushy, q.poppy)
# second = q.de_queue()
# print(q.pushy, q.poppy)
# third = q.de_queue()
# print(q.pushy, q.poppy, third)
# fourth = q.de_queue()
# print(q.pushy, q.poppy, fourth)
q.enqueue(4)
print(q.pushy, q.poppy)
########################################