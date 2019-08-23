################### Homework 4 ####################
## Crystal Caragine
## 8/22/2019
## Hw4_Caragine

my_numbers = [5,4,8,7,3,6,9]

######### Strand Sort (n)
# Start with a list of numbers, the largest number is moved to a new list.
# Then the second largest number is moved to the new list. You now have a list 
# of two numbers. Repeat the process forming a new list of two numbers every
# time. Finally, merge all the lists together. 

# creating a merged list 
def merge_lists(a,b):
    newlist = []
    while len(a) and len(b):
        if a[0] < b[0]:
            newlist.append(a.pop(0))
        else:
            newlist.append(b.pop(0))
    newlist += a 
    newlist += b 
    return newlist 

# creating a sorted sublist 
def strand(numbers):
	i, sublist = 0, [numbers.pop(0)]
	while i < len(numbers):
		if numbers[i] > sublist[-1]:
			sublist.append(numbers.pop(i))
		else:
			i += 1
	return sublist

# Combining the two methods 
def strand_sort(numbers):
	newlist = strand(numbers)
	while len(numbers):
        out = merge_list(newlist, strand(numbers))
	return out

# code based off rosettacode.org
    

######### Quick sort (n^2)
# Start with a list of numbers, identify a pivot point in the list.
# pull out numbers that are larger than the pivot point and sort them. 
# repeat this process moving the pivot point to the left or right and 
# continually sorting.     

# setting the pivote point and dividing numbers before and after that point
def part(numbers, begin, end):
    pivot_index = begin
    for i in xrange(begin+1, end+1):
        if numbers[i] <= numbers[begin]:
            pivot_index += 1
            numbers[i], numbers[pivot_idex] = numbers[pivot_idex], numbers[i]
    numbers[pivot_idex], numbers[begin] = numbers[begin], numbers[pivot_idex]
    return pivot_index

# using recursion to order the numbers and repeat
def quick_sort_recursion(numbers, begin, end):
    if begin >= end:
        return
    pivot_index = part(numbers, begin, end)
    quick_sort_recursion(numbers, begin, pivot_index-1)
    quick_sort_recursion(numbers, pivot_index+1, end)

# putting both setps together
def quick_sort(numbers, begin = 0, end= None):
    if end is None:
        end=len(numbers)-1
    return quick_sort_recursion(numbers, begin, end)

# code based offf medium-programing

quick_sort(my_numbers)


#pip install matplotlib
import matplotlib.pyplot as plt

x = range(1, 10) ## # of elements in list
y = range(1, 10) ## time
plt.subplots_adjust(left = .13, right = .95, top = .9, bottom = .3)
plt.plot(x, y)
plt.legend(['Quicksort', 'Strand Sort'], loc = "upper left", prop = {"size":10})
plt.ylabel("Time")
plt.xlabel("Elements")
plt.title("The Effect of Different Sort Algorithms on Runtime")
txt = """
"""
plt.figtext(.5, .05, txt, fontsize = 10, ha = "center")
plt.savefig('plot.pdf')
def quick_sort(my_numbers):
    return quick_sort_recursion(numbers, begin, end)
def strand_sort(numbers):
    return out
