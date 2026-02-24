# data = [('a', 5), ('b', 2), ('c', 9), ('d', 1), ('e', 7), ('f', 3), ('g', 8), ('h', 4), ('i', 6), ('j', 0)]

# sorted_data = sorted(data, key=lambda x: x[1])
# print(sorted_data)

#n  len(data)
# for i in range(n):
#     f=or j in range(0, n-i-1):
#         if data[j][1] > data[j + 1][1]:
#             data[j], data[j + 1] = data[j + 1], data[j] 
# #print(data)

# #arr = [43, 41, 23, 57, 45,12]
# sorted_arr = sorted(arr)
# print(sorted_arr)
# # n = len(arr)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j +1], arr[j]

# #print(arr)

# arr = [29, 10, 14, 37, 13]
# n = len(arr)

# # Pass 1
# min_index = 0
# for j in range(1, n):
#     if arr[j] < arr[min_index]:
#         min_index = j
#         print(min_index)
# arr[0], arr[min_index] = arr[min_index], arr[0]
# #print(arr)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:] 

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr     

*                   [38, 27, 43, 3, 9, 82, 10]
                         /              \
             [38, 27, 43]                  [3, 9, 82, 10]
               /      \                     /          \
         [38]      [27, 43]            [3, 9]        [82, 10]
                     /    \              /   \          /   \
                 [27]    [43]          [3]   [9]     [82]   [10]
At this point, every list has one element, so we stop splitting.

🔁 Merging Phase (Bottom → Up)
Now we merge sorted sublists.

Step 1: Merge single elements
[27] + [43] → [27, 43]
[3]  + [9]  → [3, 9]
[82] + [10] → [10, 82]
Step 2: Merge bigger lists
[38] + [27, 43]
→ [27, 38, 43]

[3, 9] + [10, 82]
→ [3, 9, 10, 82]
Step 3: Final merge
[27, 38, 43] + [3, 9, 10, 82]
→ [3, 9, 10, 27, 38, 43, 82]
✅ Final Sorted List
[3, 9, 10, 27, 38, 43, 82]


*2. Merge Sort has a time complexity of O(n log n). Why is it generally faster than O(n^2) algorithms like Bubble Sort for large lists?

Why O(n log n) (Merge Sort) is faster than O(n²) (Bubble Sort) for large lists
1. How fast the work grows

The key difference is how the number of operations increases as n gets bigger.

Bubble Sort (O(n²))
For every element, it compares with almost every other element.
If the list doubles in size, the work becomes about 4× more.

Merge Sort (O(n log n))
The list is:

split into halves → log n levels

merged with linear work → n per level
Total work = n × log n

📈 As n grows, n² explodes much faster than n log n.

2. Example with real numbers

Let’s compare roughly:

Number of items (n)	Bubble Sort (n²)	Merge Sort (n log n)
100	10,000	~664
1,000	1,000,000	~9,966
10,000	100,000,000	~132,877

👉 For large lists, Bubble Sort does millions more operations.

3. Bubble Sort wastes work

Keeps comparing the same elements again and again

Swaps many times

Still slow even if most of the list is already checked

Merge Sort:

Never compares unnecessarily

Each element is moved in a structured, predictable way

4. Performance scales better

Bubble Sort becomes impractical for large datasets

Merge Sort remains efficient even for thousands or millions of items


*Merge Sort requires additional memory to create the sublists. How much extra space does it need? This is known as its space complexity.

Why does Merge Sort need extra space?
Breaking it down

There are two main memory costs:

1. Temporary arrays for merging → O(n)

Even though recursion creates many sublists,

They are not all stored at the same time at full size

The largest combined temporary storage during merging is n

2. Recursion stack → O(log n)

Due to recursive function calls

One call per level of splitting

Total Space Complexity
O(n) + O(log n)  →  O(n)
Important note
;
Array-based Merge Sort → O(n) extra space

Linked-list Merge Sort → can be done in O(1) extra space (just pointer changes)

Trade-off summary
Algorithm	Time Complexity	Space Complexity
Bubble Sort	O(n²)	O(1)
Merge Sort	O(n log n)	O(n) 
 Trace the execution of Quick
*  Sort on the list [7, 2, 1, 6, 8, 5, 3, 4] using the last element as the pivot.
Let's trace the execution of Quick Sort on the list [7, 2, 1, 6, 8, 5, 3, 4] using the last element (4) as the pivot.
1. Initial List: [7, 2, 1, 6, 8, 5, 3, 4]
2. Choose Pivot: 4
3. Partitioning:
   - Elements less than 4: [2, 1, 3]
   - Elements greater than 4: [7, 6, 8, 5]
   - Pivot: [4] 
4. After Partitioning: [2, 1, 3] + [4] + [7, 6, 8, 5]
5. Recursively apply Quick Sort to the left partition [2, 1, 3]:
   - Choose Pivot: 3
   - Partitioning:
     - Elements less than 3: [2, 1]
     - Elements greater than 3: []
     - Pivot: [3]
   - After Partitioning: [2, 1] + [3] + [] 
    - Recursively apply Quick Sort to the left partition [2, 1]:
      - Choose Pivot: 1
      - Partitioning:
         - Elements less than 1: []
         - Elements greater than 1: [2]
         - Pivot: [1]
      - After Partitioning: [] + [1] + [2]
      - No further recursion needed for [] and [2]
    - No further recursion needed for [] and [3]
6. Recursively apply Quick Sort to the right partition [7, 6, 8, 5]:
   - Choose Pivot: 5
    - Partitioning:
      - Elements less than 5: [4] (already sorted)
      - Elements greater than 5: [7, 6, 8]
      - Pivot: [5]
    - After Partitioning: [4] + [5] + [7, 6, 8]
    - Recursively apply Quick Sort to the right partition [7, 6, 8]:
      - Choose Pivot: 8
      - Partitioning:
        - Elements less than 8: [7, 6]
        - Elements greater than 8: []
        - Pivot: [8]
      - After Partitioning: [7, 6] + [8] + []
      - Recursively apply Quick Sort to the left partition [7, 6]:
        - Choose Pivot: 6
        - Partitioning:
          - Elements less than 6: []
          - Elements greater than 6: [7]
          - Pivot: [6]
        - After Partitioning: [] + [6] + [7]
        - No further recursion needed for [] and [7]
      - No further recursion needed for [] and [8]
7. Final Sorted List: [1, 2, 3, 4, 5, 6, 7, 8] 

