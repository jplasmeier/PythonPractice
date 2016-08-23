# Practice with implementing a solution to the 0-1 Knapsack Problem
# Python 2.7
# J. Plasmeier | jplasmeier@gmail.com
# MIT License

# List of items, weights, and values and the max weight are from Rosetta Code
# https://rosettacode.org/wiki/Knapsack_problem/0-1#Python
import sys
sys.setrecursionlimit(1500)

def weight_of_items(items):
    if not items:
        return 0
    if type(items) is not type(items[0]):
        return items[1]
    return sum(item[1] for item in items)

def value_of_items(items, max_weight):
    if not items:
        return 0
    if type(items) is not type(items[0]):
        return items[2]
    return sum(item[2] for item in items) if sum(item[1] for item in items) < max_weight else 0

rec_count = 0
def zero_one_knapsack_rec(items, max_weight):
    global rec_count 
    rec_count += 1
    if not items:
        return ()
    head = items[0]
    tail = items[1:]
    include_head = (head,) + zero_one_knapsack_rec(tail, max_weight-head[1])
    exclude_head = zero_one_knapsack_rec(tail, max_weight)
    if value_of_items(include_head, max_weight) > value_of_items(exclude_head, max_weight):
        return include_head
    else:
        return exclude_head

def zero_one_knapsack_dp(items, max_weight, cache=None):
    global rec_count 
    rec_count += 1
    if not cache:
        cache = {}
    if not items:
        return ()
    head = items[0]
    tail = items[1:]
    if (head, max_weight) in cache:
        include_head = cache[(head, max_weight)]
    else:
        include_head = (head,) + zero_one_knapsack_dp(tail, max_weight-head[1], cache)
        cache[(head, max_weight)] = include_head
    if (tail,max_weight) in cache:
        exclude_head = cache[(tail,max_weight)]
    else:
        exclude_head = zero_one_knapsack_dp(tail, max_weight, cache)
        cache[(tail, max_weight)] = exclude_head
    if value_of_items(include_head, max_weight) > value_of_items(exclude_head, max_weight):
        return include_head
    else:
        return exclude_head

items = (
    ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
    ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
    ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
    ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
    ("socks", 4, 50), ("book", 30, 10),
    )
max_weight = 400
bring = zero_one_knapsack_dp(items, max_weight)
print 'You should bring {0}'.format(bring)
print 'It will weigh {0} and has value {1}'.format(weight_of_items(bring), value_of_items(bring,max_weight))
print 'That only took {0} recursive calls :^)'.format(rec_count)
print 'Considering n={0}...'.format(len(items))
