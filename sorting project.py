import random #generate random numbers.
import time #measures thr time algorithms are executed
import sys #allowes u to exit program safely with errors

# BUBBLE SORT
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

    bubble_sort
#bubble sort compare adjecent element , bigger numbers bubble to the end
#time complexity=0(n^2)

#INSERTION SORT
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
    arr[j+1]=arr[j]
    j-=1
    arr[j+1]=key
    return arr

#insertion sort builds the final sorted array one at a time.
# time complexity= 0(n^2)


#SELECTION SORT 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

#selection sort repeatedly selects the smallest element from the unsorted portion and moves it to the beginning.
#time complexity=0(n^2) 

# ---------------- MERGE SORT ----------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    # Merge two sorted lists into one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
# Merge sort divides the array into halves, sorts them, and merges.
# Time complexity: O(n log n) 

# ---------------- QUICK SORT ----------------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    # Elements less than or equal to pivot
    less = [x for x in arr[1:] if x <= pivot]
    # Elements greater than pivot
    greater = [x for x in arr[1:] if x > pivot]
    # Recursively sort less and greater, then combine
    return quick_sort(less) + [pivot] + quick_sort(greater)
# Quick sort selects a pivot and partitions the array around it.
# Time complexity: O(n log n) on average

 
