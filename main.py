from generate import generate_random_list
from sorting_algorithms import bubble_sort, insertion_sort, merge_sort, quick_sort
from time_utils import measure_time

def run_comparison():
    # Step 1: Choose dataset size
    while True:
        try:
            size = int(input("Enter dataset size (positive integer): "))
            if size > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Enter a number.")

    data = generate_random_list(size)

    # Step 2: Choose algorithms
    algorithms = {
        "1": ("Bubble Sort", bubble_sort),
        "2": ("Insertion Sort", insertion_sort),
        "3": ("Merge Sort", merge_sort),
        "4": ("Quick Sort", quick_sort),
        "5": ("Python Built-in", sorted)
    }

    print("\nChoose algorithm(s) to run:")
    for key, (name, _) in algorithms.items():
        print(f"{key}. {name}")
    print("6. All Algorithms")

    choices = input("Enter choice(s) (comma separated, e.g., 1,3,5): ").split(",")
    choices = [c.strip() for c in choices]

    # Step 3: Run selected algorithms
    results = {}
    if "6" in choices:
        selected = algorithms.keys()
    else:
        selected = [c for c in choices if c in algorithms]

    for c in selected:
        name, func = algorithms[c]
        results[name] = measure_time(func, data)

    # Step 4: Print results
    print(f"\nDataset Size: {size}")
    print("----------------------------")
    for name, t in results.items():
        print(f"{name}: {t:.6f} seconds")

    # Step 5: Print conclusion
    print("\nConclusion:")
    print("O(n²) algorithms (Bubble, Insertion) become slow as dataset size increases.")
    print("O(n log n) algorithms (Merge, Quick) scale much better for large datasets.")
    print("Quick Sort consistently performs best for large datasets.")
    print("Python's built-in sort is highly optimized and usually fastest for large datasets.")

def main():
    while True:
        print("\n=== Sorting Performance Comparator ===")
        print("1. Run comparison")
        print("2. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            run_comparison()
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()