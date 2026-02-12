**SORTING PERORMANCE COMPARATOR (Terminal-Based Tool)**
---
*Overview*

This project is a terminal-based sorting performance comparator designed to analyze and compare the execution time of different sorting algorithms when applied to the same dataset.

The tool helps demonstrate the practical impact of algorithmic time complexity using real execution time measurements.

*Project Goals:*

-Implement multiple sorting algorithms

-Compare their performance on identical input data

-Measure execution time accurately

-Demonstrate theoretical time complexity in practice

-Build a simple, reusable terminal application

**SORTING ALGORITHMS IMPLEMENTED**

***1 Bubble Sort:***

-Compares adjacent elements repeatedly

-Swaps elements when they are in the wrong order

-Simple to understand but inefficient for large datasets

-*TIME COMPLEXITY:* 

-Best Case: O(n)

-Average Case: O(n²)

-Worst Case: O(n²)

***2 INSERTION SORT:***
-Builds the sorted list one element at a time

-Efficient for small or nearly sorted datasets

-*TIME COMPLEXITY:*

-Best Case: O(n)

-Average Case: O(n²)

-Worst Case: O(n²)

83 MERGE SORT:*
-Uses a divide-and-conquer approach

-Recursively splits and merges lists

-*TIME COMPLEXITY:*

-Best Case: O(n log n)

-Average Case: O(n log n)

-Worst Case: O(n log n)

*QUICK SORT:*

-Selects a pivot element

-Partitions the list around the pivot

-Recursively sorts sublists

-*TIME COMPLEXITY 8

-Best Case: O(n log n)

-Average Case: O(n log n)

-Worst Case: O(n²)

***HOW THE TOOLS WORK:***

-The user runs the program from the terminal

-The user inputs the number of elements to sort

-A random dataset is generated

-Each sorting algorithm:

-Receives the same dataset

-Sorts the data independently

-Has its execution time measured

-The results are displayed in the terminal

***Performance Measurement Methodology:***

-Execution time is measured using system time

-Timing starts immediately before sorting begins

-Timing ends immediately after sorting completes

-Only the sorting process is measured

-This ensures a fair comparison across algorithms

##Sample Terminal Output:
Enter number of elements: 10000

Sorting 10000 elements...

Bubble Sort:     2.4312 seconds
Insertion Sort:  1.0875 seconds
Selection Sort:  1.9543 seconds
Merge Sort:      0.0289 seconds
Quick Sort:      0.0217 seconds

**OBSERVATIONS:**

-Quadratic algorithms (Bubble, Insertion, Selection) scale poorly

-Divide-and-conquer algorithms perform significantly better on large datasets

-Quick Sort often performs faster than Merge Sort in practice

-Performance differences increase as input size grows.

**LIMITATIONS:**

-Memory usage is not analyzed

-Execution time varies based on system performance

-Worst-case behavior of Quick Sort is not optimized in this version

**FUTURE ENHANCEMENT:**

-Optimize Quick Sort using randomized pivots

-Add graphical visualization of results

-Export results to CSV format

-Measure memory consumption

-Add command-line arguments support

**How to Run the Program:**
##python sorting project.py

*Key Learning Outcomes:*

-Understanding multiple sorting algorithms

-Practical evaluation of time complexity

-Experience with terminal-based applications

-Improved software organization and documentation

***Conclusion:***

This project highlights the importance of algorithm selection in software development.
By comparing different sorting algorithms under the same conditions, the tool provides clear evidence of how efficiency affects performance.
