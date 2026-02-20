import time
import random
import sys

# =========================
# Sorting Algorithms
# =========================

def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return arr, comparisons, swaps

def selection_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return arr, comparisons, swaps

def insertion_sort(arr):
    comparisons = 0
    swaps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j+1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break
        arr[j+1] = key
    return arr, comparisons, swaps

def merge_sort(arr):
    comparisons = 0
    swaps = 0

    def merge(left, right):
        nonlocal comparisons, swaps
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                swaps += 1
        result += left[i:]
        result += right[j:]
        return result

    def divide(lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = divide(lst[:mid])
        right = divide(lst[mid:])
        return merge(left, right)

    sorted_arr = divide(arr)
    return sorted_arr, comparisons, swaps

def quick_sort(arr):
    comparisons = 0
    swaps = 0

    def divide(lst):
        nonlocal comparisons, swaps
        if len(lst) <= 1:
            return lst
        pivot = lst[0]  # first element as pivot
        left = []
        right = []
        for x in lst[1:]:
            comparisons += 1
            if x <= pivot:
                left.append(x)
            else:
                right.append(x)
        swaps += len(left) + len(right)  # treat as swaps for counting
        return divide(left) + [pivot] + divide(right)

    sorted_arr = divide(arr)
    return sorted_arr, comparisons, swaps

# =========================
# Helper Functions
# =========================

def generate_array(size, array_type):
    if array_type == 1:  # Random
        return [random.randint(1, size*10) for _ in range(size)]
    elif array_type == 2:  # Already Sorted
        return list(range(1, size+1))
    elif array_type == 3:  # Reverse Sorted
        return list(range(size, 0, -1))
    else:
        return []

def measure_sort(sort_func, arr):
    start_time = time.time()
    sorted_arr, comparisons, swaps = sort_func(arr.copy())
    end_time = time.time()
    exec_time = end_time - start_time
    return sorted_arr, comparisons, swaps, exec_time

# =========================
# Terminal Interface
# =========================

def main():
    while True:
        print("\n=== Sorting Performance Comparator ===")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        print("6. Compare All")
        print("0. Exit")
        choice = int(input("Choose option: "))

        if choice == 0:
            print("Exiting program.")
            break

        size = int(input("Enter array size: "))
        print("Choose array type:")
        print("1. Random")
        print("2. Already Sorted")
        print("3. Reverse Sorted")
        array_type = int(input("Enter type: "))

        arr = generate_array(size, array_type)

        if choice == 1:
            sorted_arr, comp, swaps, t = measure_sort(bubble_sort, arr)
            print(f"Bubble Sort -> Time: {t:.6f}s, Comparisons: {comp}, Swaps: {swaps}")

        elif choice == 2:
            sorted_arr, comp, swaps, t = measure_sort(selection_sort, arr)
            print(f"Selection Sort -> Time: {t:.6f}s, Comparisons: {comp}, Swaps: {swaps}")

        elif choice == 3:
            sorted_arr, comp, swaps, t = measure_sort(insertion_sort, arr)
            print(f"Insertion Sort -> Time: {t:.6f}s, Comparisons: {comp}, Swaps: {swaps}")

        elif choice == 4:
            sorted_arr, comp, swaps, t = measure_sort(merge_sort, arr)
            print(f"Merge Sort -> Time: {t:.6f}s, Comparisons: {comp}, Swaps: {swaps}")

        elif choice == 5:
            sorted_arr, comp, swaps, t = measure_sort(quick_sort, arr)
            print(f"Quick Sort -> Time: {t:.6f}s, Comparisons: {comp}, Swaps: {swaps}")

        elif choice == 6:
            for func, name in [(bubble_sort,"Bubble"),(selection_sort,"Selection"),(insertion_sort,"Insertion"),
                               (merge_sort,"Merge"),(quick_sort,"Quick")]:
                sorted_arr, comp, swaps, t = measure_sort(func, arr)
                print(f"{name} Sort -> Time: {t:.6f}s, Comparisons: {comp}, Swaps: {swaps}")
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
