# ---------------- Imports ----------------
import time
from generate import generate_random_list, generate_dataset
from sorting_algorithms import bubble_sort, insertion_sort, merge_sort, quick_sort
from time_utils import measure_time
from searching_algorithms import linear_search, binary_search

# ---------------- Sorting Machine ----------------
def run_comparison():
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

    results = {}
    if "6" in choices:
        selected = algorithms.keys()
    else:
        selected = [c for c in choices if c in algorithms]

    for c in selected:
        name, func = algorithms[c]
        results[name] = measure_time(func, data)

    print(f"\nDataset Size: {size}")
    print("----------------------------")
    for name, t in results.items():
        print(f"{name}: {t:.6f} seconds")

    print("\nConclusion:")
    print("O(n²) algorithms (Bubble, Insertion) become slow as dataset size increases.")
    print("O(n log n) algorithms (Merge, Quick) scale much better for large datasets.")
    print("Quick Sort consistently performs best for large datasets.")
    print("Python's built-in sort is highly optimized and usually fastest for large datasets.")

# ---------------- Searching Machine PRO ----------------
def run_searching_machine():
    print("\n=== Searching Machine PRO: Multi-Target Mode ===")

    # Step 1: Choose dataset type
    while True:
        print("\nChoose dataset type:")
        print("1. Generate random dataset")
        print("2. Enter numbers manually")
        dataset_choice = input("Your choice: ").strip()

        if dataset_choice == "1":
            while True:
                try:
                    size = int(input("Enter dataset size (e.g., 50, 1000, 10000): "))
                    if size > 0:
                        break
                    else:
                        print("Please enter a positive integer.")
                except ValueError:
                    print("Invalid input. Enter a number.")
            data = generate_dataset(size)
            break

        elif dataset_choice == "2":
            print("Enter your numbers separated by spaces (e.g., 10 20 30 40):")
            try:
                user_input = input()
                data = [int(x) for x in user_input.strip().split()]
                if len(data) == 0:
                    print("Dataset cannot be empty.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter only numbers separated by spaces.")
        else:
            print("Invalid choice. Try again.")

    print("\nDataset ready!")
    print("Preview (first 20 numbers or less):", data[:20])
    print(f"Total numbers: {len(data)}")

    # Step 2: Enter numbers to search
    while True:
        print("\nEnter number(s) to search separated by spaces (or 'q' to quit):")
        user_input = input().strip()
        if user_input.lower() == 'q':
            break

        try:
            targets = [int(x) for x in user_input.split()]
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        for target in targets:
            print(f"\n--- Searching for: {target} ---")
            
            # Linear Search
            start = time.perf_counter()
            index, linear_comps = linear_search(data, target)
            linear_time = time.perf_counter() - start

            # Binary Search
            sorted_data = sorted(data)
            start = time.perf_counter()
            index_sorted, binary_comps = binary_search(sorted_data, target)
            binary_time = time.perf_counter() - start

            # Show results
            if index != -1:
                linear_msg = f"Linear Search → Found at index {index} | Time: {linear_time:.6f}s | Comparisons: {linear_comps}"
            else:
                linear_msg = f"Linear Search → Not found | Time: {linear_time:.6f}s | Comparisons: {linear_comps}"

            if index_sorted != -1:
                original_index = data.index(target)
                binary_msg = f"Binary Search → Found at sorted index {index_sorted}, original index {original_index} | Time: {binary_time:.6f}s | Comparisons: {binary_comps}"
            else:
                binary_msg = f"Binary Search → Not found | Time: {binary_time:.6f}s | Comparisons: {binary_comps}"

            print(linear_msg)
            print(binary_msg)

            # Highlight fastest search
            if linear_time < binary_time:
                print(">>> Linear Search was faster for this target!")
            elif binary_time < linear_time:
                print(">>> Binary Search was faster for this target!")
            else:
                print(">>> Both searches took the same time!")

    print("\nExiting Searching Machine. Goodbye!")

# ---------------- Main Menu ----------------
def main():
    while True:
        print("\n=== Data Machine ===")
        print("1. Sorting Performance Comparator")
        print("2. Searching Machine PRO")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            run_comparison()
        elif choice == "2":
            run_searching_machine()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main() 