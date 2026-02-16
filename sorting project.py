import random #generate random numbers.
import time #measures thr time algorithms are executed
import sys #allowes u to exit program safely with errors

# BUBBLE SORT
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
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
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr
#selection sort repeatedly selects the smallest element from the unsorted portion and moves it to the beginning.
#time complexity=0(n^2)
 