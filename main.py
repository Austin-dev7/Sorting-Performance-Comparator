from sorting_algorithms import bubble_sort, insertion_sort, merge_sort, quick_sort
from generate import generate_random_list
from time_utils import measure_time

# Ask user for dataset size
size = int(input("Enter the size of the dataset to sort: "))
data = generate_random_list(size)

# Measure time for each algorithm
results = {
    "Bubble Sort": measure_time(bubble_sort, data),
    "Insertion Sort": measure_time(insertion_sort, data),
    "Merge Sort": measure_time(merge_sort, data),
    "Quick Sort": measure_time(quick_sort, data)
}

# Find the fastest algorithm
fastest_algorithm = min(results, key=results.get)

# Print results in a neat table
print("\nSorting Performance Results")
print(f"{'Algorithm':<15} {'Time (seconds)':<15}")
print("-"*30)
for algo, t in results.items():
    print(f"{algo:<15} {t:<15.6f}")

print(f"\nFastest algorithm: {fastest_algorithm} ({results[fastest_algorithm]:.6f} seconds)")

  
