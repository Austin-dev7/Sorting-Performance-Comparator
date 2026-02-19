 # Sorting Performance Comparator

## Project Overview
This project compares the performance of different sorting algorithms by measuring how long they take to sort datasets of different sizes.  
It demonstrates the practical differences between algorithms with different time complexities.

## Algorithms Implemented
- **Bubble Sort** – O(n²)  
- **Insertion Sort** – O(n²)  
- **Merge Sort** – O(n log n)  
- **Quick Sort** – O(n log n) (average case)  
- **Python Built-in Sort** – Highly optimized

Key Observation

O(n²) algorithms become significantly slower as data grows.

O(n log n) algorithms scale efficiently.

Python’s built-in sort is highly optimized and performs best.

⚙️ How the Program Works

* The program runs in the terminal.

* A dataset of predefined sizes (100, 1000, 10000) is generated.

* Each algorithm receives the same dataset.

* Execution time is measured independently.

* Results are displayed in a structured format.

* A performance conclusion is printed.

🏗

## Files and Purpose
| File | Responsibility |
|------|----------------|
| `main.py` | Runs the program and prints results |
| `generate.py` | Generates random datasets |
| `sorting_algorithms.py` | Contains sorting algorithm implementations |
| `time_utils.py` | Measures execution time |

## How to Run
1. Make sure all files are in the same folder.  
2. Open a terminal or PowerShell in the project folder.  
3. Run the program with:
   ```bash
   python main.py
