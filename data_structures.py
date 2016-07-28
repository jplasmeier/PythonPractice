# Practice With Stacks and Queues
# Python 2.7
# J. Plasmeier | jplasmeier@gmail.com
# MIT License

class Queue:

    def __init__(self):
        self.items = []

    def enque(self, element):
        self.items.append(element)

    def deque(self):
        item = self.items[:1]
        self.items = self.items[1:]
        return item
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)




