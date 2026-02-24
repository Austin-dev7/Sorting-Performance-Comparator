from generate import generate_random_list
from sorting_algorithms import bubble_sort, insertion_sort, merge_sort, quick_sort
from time_utils import measure_time


def run_comparison():
    sizes = [100, 1000, 10000]

    print("Sorting Performance Comparison\n")

    for size in sizes:
        print(f"\nDataset Size: {size}")
        print("----------------------------")

        data = generate_random_list(size)

        # Measure each sorting algorithm
        bubble_time = measure_time(bubble_sort, data)
        insertion_time = measure_time(insertion_sort, data)
        merge_time = measure_time(merge_sort, data)
        quick_time = measure_time(quick_sort, data)
        python_time = measure_time(sorted, data)  # Python built-in sort

        # Print results
        print(f"Bubble Sort:          {bubble_time:.6f} seconds")
        print(f"Insertion Sort:       {insertion_time:.6f} seconds")
        print(f"Merge Sort:           {merge_time:.6f} seconds")
        print(f"Quick Sort:           {quick_time:.6f} seconds")
        print(f"Python Built-in Sort: {python_time:.6f} seconds")

    # Print conclusion after all dataset sizes
    print("\nConclusion:")
    print("O(n²) algorithms (Bubble, Insertion) become slow as dataset size increases.")
    print("O(n log n) algorithms (Merge, Quick) scale much better for large datasets.")
    print("Quick Sort consistently performs best for large datasets.")
    print("Python's built-in sort is highly optimized and usually fastest for large datasets.")


def main():
    while True:
        print("\n=== Sorting Performance Comparator ===")
        print("1. Run full comparison")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            run_comparison()  # your existing function
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()