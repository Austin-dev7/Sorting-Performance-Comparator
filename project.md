Sorting Performance Comparator (Terminal Tool)
1. Introduction

Sorting algorithms are fundamental in computer science.
Although many sorting algorithms exist, they differ greatly in performance, especially as the size of the data increases.

This project is a terminal-based sorting performance comparator that measures and compares the execution time of different sorting algorithms on the same dataset.

2. Project Objectives

The objectives of this project are:

To implement multiple sorting algorithms

To compare their execution time using real data

To demonstrate the practical impact of time complexity

To build a simple and reusable terminal tool

3. Sorting Algorithms Used:

3.1 Bubble Sort
Repeatedly compares adjacent elements
Swaps them if they are in the wrong order
Simple but inefficient for large datasets

Time Complexity:
Best case: O(n)
Average/Worst case: O(n²)

3.2 Insertion Sort
Builds the sorted list one element at a time

Efficient for small or nearly sorted datasets

Time Complexity:
Best case: O(n)
Average/Worst case: O(n²)

3.3 Merge Sort:
Uses a divide-and-conquer approach
Recursively splits the list and merges sorted halves

Time Complexity:
Best/Average/Worst case: O(n log n)

4. Project Structure
sorting-performance-comparator/

├── sorting project.py  # Main terminal program
├── README              # about project
└── utils.py            # Helper functions

5. How the Tool Works

The user runs the program from the terminal

The user inputs the number of elements to sort

A random list of numbers is generated

Each sorting algorithm sorts the same dataset

Execution time for each algorithm is measured

Results are displayed in the terminal

6. Measuring Performance

The program measures performance by:

Recording the start time before sorting

Executing the sorting algorithm

Recording the end time after sorting

Calculating the time difference

This ensures that only the sorting process is measured.

7. Sample Terminal Output
Enter number of elements: 10000

Sorting 10000 elements...

Bubble Sort: 2.4312 seconds
Insertion Sort: 1.0875 seconds
Merge Sort: 0.0289 seconds

8. Why Performance Differs

The performance difference occurs because:

Bubble Sort and Insertion Sort have quadratic time complexity

Merge Sort has logarithmic growth

As input size increases, inefficient algorithms slow down rapidly

This project visually proves theoretical time complexity using real execution time.

9. Limitations

Bubble Sort and Insertion Sort are not suitable for large datasets

Execution time may vary slightly due to system performance

Memory usage is not measured in this version

10. Future Improvements

Add Quick Sort for further comparison

Visualize results using graphs

Export results to a CSV file

Add command-line arguments for automation

11. Conclusion

This terminal-based sorting performance comparator demonstrates how different sorting algorithms behave in practice.
It highlights the importance of choosing efficient algorithms when working with large datasets.

12. How to Run the Program
python sortin project.py

13. Key Learning Outcomes

Understanding of sorting algorithms

Practical application of time complexity

Experience with terminal-based tools

Writing clean, documented code using Markdown