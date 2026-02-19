1️⃣ Project Objective

The goal of this project is to compare the performance of different sorting algorithms by measuring how long they take to sort datasets of different sizes.

This helps demonstrate the practical difference between algorithms with different time complexities.

2️⃣ System Overview

The system is divided into separate modules (files), each with a specific responsibility:

File	Responsibility
main.py	Controls the program flowgenerate.py	Generates random datasets
sorting_algorithms.py	Contains sorting implementations
time_utils.py	Measures execution time

3️⃣ Program Flow

The user enters the dataset size.

generate.py creates a list of random numbers.

Each sorting algorithm sorts the same dataset.

time_utils.py measures how long each algorithm takes.

The program prints the results in a table.

The fastest algorithm is identified and displayed.

4️⃣ Algorithms Used
Algorithm	Time Complexity
Bubble Sort	O(n²)
Insertion Sort	O(n²)
Merge Sort	O(n log n)
Quick Sort	O(n log n) (average case) 


        +-------------------+
        |     User Input    |
        | (Dataset Size)    |
        +---------+---------+
                  |
                  v
        +-------------------+
        |   generate.py     |
        | Generates Dataset |
        +---------+---------+
                  |
                  v
        +-------------------+
        | sorting_algorithms|
        |  (Bubble, Merge,  |
        |   Quick, etc.)    |
        +---------+---------+
                  |
                  v
        +-------------------+
        |   time_utils.py   |
        | Measures Runtime  |
        +---------+---------+
                  |
                  v
        +-------------------+
        |     main.py       |
        | Displays Results  |
        +-------------------+
   +-------------------+
        |     main.py       |
        | Displays Results  |
        +-------------------+

---

### Results Overview (Example)

| Algorithm           | Dataset 100 | Dataset 1,000 | Dataset 10,000 |
|--------------------|------------|---------------|----------------|
| Bubble Sort         | 0.000558 s | 0.083614 s    | 7.85 s         |
| Insertion Sort      | 0.000245 s | 0.042045 s    | 4.03 s         |
| Merge Sort          | 0.000244 s | 0.003034 s    | 0.043 s        |
| Quick Sort          | 0.000210 s | 0.003904 s    | 0.023 s        |
| Python Built-in     | 0.000014 s | 0.000148 s    | 0.001 s        |

**Conclusion:**  
- O(n²) algorithms (Bubble, Insertion) are slow for large datasets.  
- O(n log n) algorithms (Merge, Quick) scale much better.  
- Python’s built-in sort is highly optimized and usually fastest.