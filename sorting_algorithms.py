'''
Sorting Algorithms implemented in Python2
'''
import random

def insertion_sort(list):
    return list

def generate_random_array(size):
    random_array = []
    for i in range(0,size):
        random_array.append(random.randint(0,size*2))
    return random_array

arr = generate_random_array(100)
print arr
print insertion_sort(arr)
