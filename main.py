Ask the user for dataset size

Generate random data

Run all sorting algorithms

Measure their time

Print the results

Show the fastest one


from generate import generate_random_list
from sorting_algorithms import bubble_sort, insertion_sort, merge_sort, quick_sort
from time_utils import measure_time


def main():
    # Ask user for dataset size
    size = int(input("Enter the size of the dataset to sort: "))

    # Generate random data
    data = generate_random_list(size)

    print("\nSorting Performance Results")
    print("Algorithm       Time (seconds)")
    print("------------------------------")

    # Measure time for each algorithm
    bubble_time = measure_time(bubble_sort, data)
    print(f"Bubble Sort     {bubble_time:.6f}")

    insertion_time = measure_time(insertion_sort, data)
    print(f"Insertion Sort  {insertion_time:.6f}")

    merge_time = measure_time(merge_sort, data)
    print(f"Merge Sort      {merge_time:.6f}")

    quick_time = measure_time(quick_sort, data)
    print(f"Quick Sort      {quick_time:.6f}")

    # Find fastest algorithm
    times = {
        "Bubble Sort": bubble_time,
        "Insertion Sort": insertion_time,
        "Merge Sort": merge_time,
        "Quick Sort": quick_time
    }

    fastest = min(times, key=times.get)
    print(f"\nFastest algorithm: {fastest} ({times[fastest]:.6f} seconds)")


if __name__ == "__main__":
    main()
