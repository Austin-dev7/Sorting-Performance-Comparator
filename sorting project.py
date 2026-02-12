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
