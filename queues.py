# Practice With Stacks and Queues
# Python 2.7
# J. Plasmeier | jplasmeier@gmail.com
# MIT License
import random,copy

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
    
    def peek(self):
        return self.items[:1]

    def queue_sum(self):
        total = 0;
        for item in self.items:
            total = total + item
        return total
    
    def clear(self):
        self.items = []
    
    def __str__(self):
        return ' '.join(str(e) for e in self.items)

def test_queue():
	q = Queue()
	print q.isEmpty()
	q.enque(3)
	q.enque(5)
	q.enque(7)
	print q.size()
	print q.deque()
	print q.deque()
	print q.deque()
	print q.isEmpty()

def racetrack(all_laps, trials):
    # Given a list of all lap times, find the shortest sequence of trials number of laps.
    q = Queue()
    fastest = Queue()
    for lap in all_laps:
        if q.size() < trials:
            q.enque(lap)
            if q.size() == trials and fastest.isEmpty():
                fastest = copy.deepcopy(q)
        elif lap < q.peek():
            q.deque()
            q.enque(lap)
            if q.queue_sum() < fastest.queue_sum():
                fastest = copy.deepcopy(q)
        else:
            if q.queue_sum() < fastest.queue_sum():
                fastest = copy.deepcopy(q)
            q.clear()
    return fastest






all_laps = [random.random()*100 for x in range(0,100)]
#all_laps = [100-x for x in range(0,100)]
#all_laps = range(0,100)
trials = 10
#print all_laps
f = racetrack(all_laps, trials)
print f

