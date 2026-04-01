def linear_search(arr, target):
    comparisons = 0
    for i, num in enumerate(arr):
        comparisons += 1
        if num == target:
            return i, comparisons
    return -1, comparisons


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    comparisons = 0

    while left <= right:
        comparisons += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, comparisons






