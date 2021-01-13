import random
import time
import copy
from datetime import datetime

# * This file contains many different sorting algorithms and compares their time complexities in sorting different sizes of data.
# * The user can enter the size of data being sorted and the program produces the amount of time taken to achieve that.
# ? The objective of this program was to simply gain more experience with algorithm design and practice using more Python features such as working with date and time.

# TODO: Add a visualizer to show the list being sorted, let the user select which algorithm they wish to see, and rewrite code using Object Oriented Programming principles.
# TODO: Add Radix Sort, Cocktail Sort, Gnome Sort, Heap Sort, Bitonic Sort, and Bucket Sort.
# This file will continue to be updated on Github. Current sorting algorithms: Insertion Sort, Selection Sort, Bubble Sort, Merge Sort, Shell Sort, and Quick Sort.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Welcome to the Sorting Algorithms Time Complexity Comparison Tool! Enter a number from 1-5 which corresponds - ")
print("to data sizes of 500, 1000, 5000, 10000, and 25000 respectively. Your choice determines the size of the random unsorted list.")


setting1 = 500
setting2 = 1000
setting3 = 5000
setting4 = 10000
setting5 = 25000


# Insertion Sort-------------------------------------------


def insertion_sort(lst):
    for i in range(1, len(lst)):
        for j in range(i-1, -1, -1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            else:
                break

# Selection Sort-------------------------------------------


def selection_sort(lst):
    for i in range(0, len(lst) - 1):
        minIndex = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[minIndex]:
                minIndex = j
        if minIndex != i:
            lst[i], lst[minIndex] = lst[minIndex], lst[i]

# Bubble Sort----------------------------------------------


def bubble_sort(lst):
    for i in range(0, len(lst) - 1):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

# Shell Sort-----------------------------------------------


def shell_short(lst):
    gap = len(lst) // 2

    while gap > 0:
        for i in range(gap, len(lst)):
            temp = lst[i]
            j = i
            while j >= gap and lst[j-gap] > temp:
                lst[j] = lst[j-gap]
                j -= gap
            lst[j] = temp

        gap //= 2


# Merge Sort-----------------------------------------------

def merge_sort(lst=[]):
    if lst == []:
        pass
    if len(lst) < 2:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    lst = result
    return result

# Quick Sort-----------------------------------------------


# def quick_sort(lst=[], start=0, end=0):
#    if lst == []:
#        end = len(lst) - 1
#    if start < end:
#        pivot = partition(lst, start, end)
#        quick_sort(lst, start, pivot-1)
#        quick_sort(lst, pivot+1, end)


# def partition(lst, start, end):
#    x = lst[end]
#    i = start-1
#    for j in range(start, end+1, 1):
#        if lst[j] <= x:
#            i += 1
#            if i < j:
#                lst[i], lst[j] = lst[j], lst[i]
#    return i


choice = input("Enter a number from 1 to 5: ")

print("----------------------------Time Complexity Results------------------------------")
print("Note that the time displayed is in milliseconds.")
if choice == str(1):
    w = [random.randint(0, 10000000) for a in range(0, setting1)]
    start = time.time()
    insertion_sort(w)
    end = time.time()
    print("Insertion Sort ( size =", str(setting1), "): ", (end - start) * 1000)

    w = [random.randint(0, 10000000) for a in range(0, setting1)]
    start = time.time()
    selection_sort(w)
    end = time.time()
    print("Selection Sort ( size =", str(setting1), "): ", (end - start) * 1000)

    w = [random.randint(0, 10000000) for a in range(0, setting1)]
    start = time.time()
    bubble_sort(w)
    end = time.time()
    print("Bubble Sort ( size =", str(setting1), "): ", (end - start) * 1000)

    w = [random.randint(0, 10000000) for a in range(0, setting1)]
    start = time.time()
    shell_short(w)
    end = time.time()
    print("Shell Sort ( size =", str(setting1), "): ", (end - start) * 1000)

    w = [random.randint(0, 10000000) for a in range(0, setting1)]
    start = time.time()
    merge_sort(w)
    end = time.time()
    print("Merge Sort ( size =", str(setting1), "): ", (end - start) * 1000)

elif choice == str(2):
    w = [random.randint(0, 10000000) for a in range(0, setting2)]
    start = time.time()
    insertion_sort(w)
    end = time.time()
    print("Insertion Sort ( size =", str(setting2), "): ", (end - start) * 1000)

    w = [random.randint(0, 10000000) for a in range(0, setting2)]
    start = time.time()
    selection_sort(w)
    end = time.time()
    print("Selection Sort ( size =", str(setting2), "): ", (end - start) * 1000)

    w = [random.randint(0, 10000000) for a in range(0, setting2)]
    start = time.time()
    bubble_sort(w)
    end = time.time()
    print("Bubble Sort ( size =", str(setting2), "): ", (end - start) * 1000)

    w = [random.randint(0, 10000000) for a in range(0, setting2)]
    start = time.time()
    shell_short(w)
    end = time.time()
    print("Shell Sort ( size =", str(setting2), "): ", (end - start) * 1000)

    w = [random.randint(0, 10000000) for a in range(0, setting2)]
    start = time.time()
    merge_sort(w)
    end = time.time()
    print("Merge Sort ( size =", str(setting2), "): ", (end - start) * 1000)

elif choice == str(3):
    w = [random.randint(0, 10000000) for a in range(0, setting3)]
    start = time.time()
    insertion_sort(w)
    end = time.time()
    print("Insertion Sort ( size =", str(setting3), "): ", (end - start) * 1000)

    w = [random.randint(0, 10000000) for a in range(0, setting3)]
    start = time.time()
    selection_sort(w)
    end = time.time()
    print("Selection Sort ( size =", str(setting3), "): ", (end - start) * 1000)

    w = [random.randint(0, 10000000) for a in range(0, setting3)]
    start = time.time()
    bubble_sort(w)
    end = time.time()
    print("Bubble Sort ( size =", str(setting3), "): ", (end - start) * 1000)

    w = [random.randint(0, 10000000) for a in range(0, setting3)]
    start = time.time()
    shell_short(w)
    end = time.time()
    print("Shell Sort ( size =", str(setting3), "): ", (end - start) * 1000)

    w = [random.randint(0, 10000000) for a in range(0, setting3)]
    start = time.time()
    merge_sort(w)
    end = time.time()
    print("Merge Sort ( size =", str(setting3), "): ", (end - start) * 1000)

elif choice == str(4):
    w = [random.randint(0, 10000000) for a in range(0, setting4)]
    start = time.time()
    insertion_sort(w)
    end = time.time()
    print("Insertion Sort ( size =", str(setting4), "): ", (end - start) * 1000)

    w = [random.randint(0, 10000000) for a in range(0, setting4)]
    start = time.time()
    selection_sort(w)
    end = time.time()
    print("Selection Sort ( size =", str(setting4), "): ", (end - start) * 1000)

    w = [random.randint(0, 10000000) for a in range(0, setting4)]
    start = time.time()
    bubble_sort(w)
    end = time.time()
    print("Bubble Sort ( size =", str(setting4), "): ", (end - start) * 1000)

    w = [random.randint(0, 10000000) for a in range(0, setting4)]
    start = time.time()
    shell_short(w)
    end = time.time()
    print("Shell Sort ( size =", str(setting4), "): ", (end - start) * 1000)

    w = [random.randint(0, 10000000) for a in range(0, setting4)]
    start = time.time()
    merge_sort(w)
    end = time.time()
    print("Merge Sort ( size =", str(setting4), "): ", (end - start) * 1000)

elif choice == str(5):
    w = [random.randint(0, 10000000) for a in range(0, setting5)]
    start = time.time()
    insertion_sort(w)
    end = time.time()
    print("Insertion Sort ( size =", str(setting5), "): ", (end - start) * 1000)

    w = [random.randint(0, 10000000) for a in range(0, setting5)]
    start = time.time()
    selection_sort(w)
    end = time.time()
    print("Selection Sort ( size =", str(setting5), "): ", (end - start) * 1000)

    w = [random.randint(0, 10000000) for a in range(0, setting5)]
    start = time.time()
    bubble_sort(w)
    end = time.time()
    print("Bubble Sort ( size =", str(setting5), "): ", (end - start) * 1000)

    w = [random.randint(0, 10000000) for a in range(0, setting5)]
    start = time.time()
    shell_short(w)
    end = time.time()
    print("Shell Sort ( size =", str(setting5), "): ", (end - start) * 1000)

    w = [random.randint(0, 10000000) for a in range(0, setting5)]
    start = time.time()
    merge_sort(w)
    end = time.time()
    print("Merge Sort ( size =", str(setting5), "): ", (end - start) * 1000)
