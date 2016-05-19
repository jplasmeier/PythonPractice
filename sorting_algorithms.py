'''
Sorting Algorithms implemented in Python2
Code borrowed from RosettaCode.com
'''
import random
from math import log
'''
Insertion Sort - a basic sorting algorithm that searches the list for the minimum element
                 and appends that element to a sorted subarry at the beginning of the list.

Runtime - O(n^2) average, O(n^2) worst-case

Memory - O(1)

'''
def insertion_sort(l):
    for i in xrange(1, len(l)):
        j = i-1 
        key = l[i]
        while (l[j] > key) and (j >= 0):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

'''
Bubble Sort - another basic sorting algorithm that swaps pairs of elements until the list is ordered.

Runtime - O(n^2) average, O(n^2) worst-case

Memory - O(1)
'''
def bubble_sort(seq):
    """Inefficiently sort the mutable sequence (list) in place.
       seq MUST BE A MUTABLE SEQUENCE.
 
       As with list.sort() and random.shuffle this does NOT return 
    """
    changed = True
    while changed:
        changed = False
        for i in xrange(len(seq) - 1):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                changed = True
    return seq

'''
merge - an auxiliary function for Merge Sort. Takes two lists and merges them into a sorted list.
'''
def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
 
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result

'''
Merge Sort - a more advanced sorting algorithm which works by recurisvely splitting the list down to pairs
             and then merging sorted pairs upto the entire list. Requires auxiliary function merge(left, right)
             to run.

Runtime - O(n*log(n)) average, O(n*log(n)) worst-case

Memory - O(n) - space required to merge lists
'''
def merge_sort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

'''
Quick Sort - a more advanced sorting algorithm that works by recursively partitioning the list by
             a certain pivot. 

Runtime - O(n log(n)) average, O(n^2) worst-case

Memory - O(log(n)) 
'''
def quick_sort(l):
    less = []
    pivot_list = []
    more = []
    if len(l) <= 1:
        return l
    else:
        pivot = l[0]
        for i in l:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivot_list.append(i)
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivot_list + more
    
def getDigit(num, base, digit_num):
    # pulls the selected digit
    return (num // base ** digit_num) % base  
 
def makeBlanks(size):
    # create a list of empty lists to hold the split by digit
    return [ [] for i in range(size) ]  
 
def split(a_list, base, digit_num):
    buckets = makeBlanks(base)
    for num in a_list:
        # append the number to the list selected by the digit
        buckets[getDigit(num, base, digit_num)].append(num)  
    return buckets
 
# concatenate the lists back in order for the next step
def radix_merge(a_list):
    new_list = []
    for sublist in a_list:
       new_list.extend(sublist)
    return new_list
 
def maxAbs(a_list):
    # largest abs value element of a list
    return max(abs(num) for num in a_list)
 
def split_by_sign(a_list):
    # splits values by sign - negative values go to the first bucket,
    # non-negative ones into the second
    buckets = [[], []]
    for num in a_list:
        if num < 0:
            buckets[0].append(num)
        else:
            buckets[1].append(num)
    return buckets

'''
Radix Sort - A fast numerical sort that sorts numbers starting at the ones digit and moving towards the 
             largest numbers' largest digit. Base is variable and given by a parameter.

Runtime - O(n*k) absolute - where k is the number of passes (the number of places/digits under the base
''' 
def radix_sort(a_list, base):
    # there are as many passes as there are digits in the longest number
    passes = int(round(log(maxAbs(a_list), base)) + 1) 
    new_list = list(a_list)
    for digit_num in range(passes):
        new_list = radix_merge(split(new_list, base, digit_num))
    return radix_merge(split_by_sign(new_list))

'''
Binary Search - a search algorithm that works by picking the number in the middle of the range of values
                then picks the side which the value being searched is in and picks a number in the middle
                of that list and on and on.
'''
def binary_search(l, value):
    low = 0
    high = len(l)-1
    while low <= high: 
        mid = (low+high)//2
        if l[mid] > value: high = mid-1
        elif l[mid] < value: low = mid+1
        else: return mid
    return -1

def generate_random_array(size):
    random_array = []
    for i in range(0,size):
        random_array.append(random.randint(0,size*2))
    return random_array

arr = generate_random_array(100)
print "unsorted\n"
print arr
print "sorted\n"
sorted_arr = radix_sort(arr,10)
print binary_search(sorted_arr, sorted_arr[23])
print sorted_arr
