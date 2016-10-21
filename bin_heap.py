# Binary Min Heap in Python 2.7

class BinaryHeap(object):
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def sift_up(self, i):
        while i / 2 > 0:
            if self.heap_list[i] < self.heap_list[i/2]:
                tmp = self.heap_list[i/2]
                self.heap_list[i/2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i / 2

    def sift_down(self, i):
        while (i * 2) <= self.current_size:
            min_child = self.get_min_child(i)
            if self.heap_list[i] > self.heap_list[min_child]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[min_child]
                self.heap_list[min_child] = tmp
            i = min_child

    def get_min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i*2
            else:
                return i * 2 + 1

    def del_min(self):
        value = self.heap_list[1]
        self.current_size -= 1
        self.heap_list[1] = self.heap_list[self.current_size]
        self.heap_list.pop()
        self.sift_down(1)
        return value

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.sift_up(self.current_size)

    def build_heap_from_list(self,lst):
        i = len(lst) / 2
        self.heap_list = [0] + lst
        self.current_size = len(lst)
        while i > 0:
            self.sift_down(i)
            i -= 1

    def __str__(self):
        return ' '.join(str(e) for e in self.heap_list)

h1 = BinaryHeap()
h1.build_heap_from_list([5,42,23,8,5,234,75])
print h1
