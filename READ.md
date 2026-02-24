
# 📊 Sorting Performance Comparator

This project compares the performance of different sorting algorithms by measuring how long they take to sort datasets of different sizes.

It demonstrates the practical differences between algorithms with different time complexities and shows how efficiency impacts real-world execution time.

---

## 🧠 Algorithms Implemented

- Bubble Sort – O(n²)  
- Insertion Sort – O(n²)  
- Merge Sort – O(n log n)  
- Quick Sort – O(n log n) (average case)  
- Python Built-in Sort (sorted()) – Highly optimized (Timsort)  

---

## ⚙️ How the Program Works

1. Run the program in the terminal:

```bash
python main.py
Choose dataset size (e.g., 1000)

Choose which algorithm(s) to run:

Bubble Sort
Insertion Sort
Merge Sort
Quick Sort

All Algorithms

The program will measure the execution time of the selected algorithm(s) and display the results in a structured format.

# A conclusion is printed at the end.

📈 Example Output

Enter dataset size: 1000
Choose algorithm(s) to run: 2,3,5

Dataset Size: 1000
----------------------------
Insertion Sort:       0.423 seconds
Merge Sort:           0.004 seconds
Python Built-in:      0.001 seconds

Conclusion:
O(n log n) algorithms significantly outperform O(n²) algorith

🏗 Project Structure
File	Responsibility
main.py	Runs the interactive program
generate.py	Generates random datasets
sorting_algorithms.py	Contains sorting algorithm implementations
time_utils.py	Measures execution time

▶️ How to Run

Make sure all files are in the same folder

Open a terminal in the project folder

Run:

python main.py