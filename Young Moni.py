 # # creat_of_file_python
#
# # time = open("young.py",'w')
# # # time.write("i am a girl")
# # #
# # # money = open("ebuka.py",'w')
# # # money.write("i have money")
# #
# # try:
# #     with open("ebuka.py",'r' ) as f:
# #         content = f.readlines()
# #         print(content)
# # # except IOError as e:
# #
# #     list_to_creat = {"here is line 1. \n",
# #                      "here is line 3. \n",
# #                      "here is line .  \n"}
# #     try:
# #          with open("augustine.py",'w') as file:
# #              file.write("list_to_creat").
# # except IOError as e:
# #         print(f"An error occurred writing: {e}")
#
# data_base
#
# import sqlite3
# import os
# from os.path import exists
#
# DB_file = "example.db"
#
# if os.path.exists(DB_file):
#     print(f"it exists")
# else:
#     print("nothing there")
#
#     try:
#         conn = sqlite3.connect(DB_file)
#         print("connected")
#     except sqlite3.SQLITE_ERROR as e:
#         print({e})
# #
#     try:
#         cursor = conn.cursor()

#         creat_table_query = """
#         CREAAT TABLE IF NOT EXISTS users (
#            id INTEGER PRIMARY KEY,
#            name TEXT NOT NULL,
#            emil TEXT NOT NULL UNIQUE
#         );
#         """
#         cursor.execute(creat_table_query)
#         print("Table 'users' created sucessfully (if it didn't exist).")

#    try:
#    except IOError as e:


# import sqlite3
# import os
# DB_FILE = "austine.db"
# connection = sqlite3.connect('austine.db')
# if os.path.exists(DB_FILE):
#     print("the database file exists")
# else:
#     print("nothing is there")

# try:
#     conn = sqlite3.connect(DB_FILE)
#     print("connected to database")
# except sqlite3.Error as e:
#     print(e)

# import tkinter as tk
# root = tk.Tk() 
# root.title("Young Money App") 
# root.geometry("400x300") 
# root.mainloop()

# # root=tk.Tk()
# # root.title()
# # import tkinter as tk

# # def on_button_click():
# #     print("button clicked!")
    
# # # =tk.Trootk()
# # button=tk.button(root,text="click me" , command=on_button_click) 
# # button.pack()
# # root.mainloop()
# import tkinter as tk

# def on_button_click():
#     print("Button clicked!")

# root = tk.Tk()
# button = tk.Button(root, text="click me", command=on_button_click)
# button.pack()
# root.mainloop()


# root = tk.TK()

# root.title("Your App")

# lable = tk.Lable(root, text="Hello,Tkinter!")
# def on_button_click():
#     print("button click")

    
#     button = 


    

# name = input ("my name is")
# print(name)


# age = int(input ("enter age:"))
# print(age) 

# input = float(input("the amount is:"))
# print(amount) 

# result = bool(input("do you have money?: "))
# print(result) 

# arr = [4,8,9,7,6,12] # list [0,1,2,3,4,5,]

# def b_sort(arr) :
#     n = len(arr)
#     for i in range(n) :
#         swapp = False
        
#         for j in range(0, n-i-1):
            
#             if arr[j] > arr[j + 1]:
#                 temp = arr[j]
#                 arr[j] = arr[j + 1]  
#                 arr[j+1] = temp
#swapp = True
#         if not swapp:
#             break
#     return arr
# sorted_list = b_sort
# my_list = b_sort(arr)
# print(my_list)    
                  
# def insertion_sort(strings):
#     for i in range(1, len(strings)):
#         key = strings[i]
#         j = i - 1
#         while j >= 0 and key < strings[j]:
#             strings[j + 1] = strings[j]
#             j -= 1
#         strings[j + 1] = key
#     return strings 

# WORDS = ["banana", "apple", "orange", "grape", "kiwi"]
# sorted_words = insertion_sort(WORDS)
# print("Sorted words:", sorted_words) 

arr = [43, 41, 23, 57, 45,12]
def selection_sort(arr):
    n = len(arr)
    for i in range(len(arr)):
       # print(j)
        min_index = i
        for j in range(i + 1, len(arr)):
            #print(j)
            #print(arr[j])
            if arr[j] < arr[min_index]:
                min_index = j
                #print(min_index) 
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
    selection_sort(arr)
    
    
    """
    pass 1 (i = 0):
    1 = 0, min_index = 0(initally pointing to 43)
    '''
    **inner loop serches for minimum element in the unsorted array**
    j=1: arr[0]=43 > arr[1]=41? YES -> min_index=1
    j=2: arr[1]=41 > arr[2]=23? YES -> min_index=2
    j=3: arr[2]=23 > arr[3]=57? NO  -> min_index=2
    j=4: arr[2]=23 > arr[4]=45? NO  -> min_index=2
    j=5: arr[2]=23 > arr[5]=12? YES -> min_index=5
    '''
    **Result:** minimum is 12 at index 5
    swap arr[0] and arr[5] -> [12, 41, 23, 57, 45, 43]
    '''
    before: [43, 41, 23, 57, 45, 12]
             i=0              min_index=5
    after:  [12, 41, 23, 57, 45, 43]
    
    pass 2 (i = 1):
    min_index = 1(initally pointing to 41)
    '''
    j=2: arr[1]=41 > arr[2]=23? YES -> min_index=2
    j=3: arr[2]=23 > arr[3]=57? NO  -> min_index=2
    j=4: arr[2]=23 > arr[4]=45? NO  -> min_index=2
    j=5: arr[2]=23 > arr[5]=43? NO  -> min_index=2
    '''
    **Result:** minimum is 23 at index 2
    swap arr[1] and arr[2] -> [12, 23, 41, 57, 45, 43]
    '''
    before: [12, 41, 23, 57, 45, 43]
              i=1          min_index=2  
              
    after:  [12, 23, 41, 57, 45, 43]
    
    pass 3 (i = 2):
    min_index = 2(initally pointing to 41)
    '''
    j=3: arr[2]=41 > arr[3]=57? NO  -> min_index=2
    j=4: arr[2]=41 > arr[4]=45? NO  -> min_index=2
    j=5: arr[2]=41 > arr[5]=43? NO  -> min_index=2
    '''
    **Result:** minimum is 41 at index 2
    no swap needed
    '''
    before: [12, 23, 41, 57, 45, 43]
               i=2       min_index=2
    after:  [12, 23, 41, 57, 45, 43]
    
    pass 4 (i = 3):
    min_index = 3(initally pointing to 57)
    '''
    j=4: arr[3]=57 > arr[4]=45? YES -> min_index=4
    j=5: arr[4]=45 > arr[5]=43? YES -> min_index=5
    '''
    **Result:** minimum is 43 at index 5
    swap arr[3] and arr[5] -> [12, 23, 41, 43, 45, 57]
    '''
    before: [12, 23, 41, 57, 45, 43]
                 i=3          min_index=5
    after:  [12, 23, 41, 43, 45, 57]
    
    pass 5 (i = 4):
    min_index = 4(initally pointing to 45)
    '''
    j=5: arr[4]=45 > arr[5]=57? NO  -> min_index=4
    '''     
    **Result:** minimum is 45 at index 4
    no swap needed
    '''
    before: [12, 23, 41, 43, 45, 57]
                   i=4      min_index=4 
    after:  [12, 23, 41, 43, 45, 57]
    pass 6 (i = 5):
    min_index = 5(initally pointing to 57)  
    **Result:** minimum is 57 at index 5
    no swap needed
    '''
    before: [12, 23, 41, 43, 45, 57]
                     i=5  min_index=5
    after:  [12, 23, 41, 43, 45, 57]
    """
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)   
  
merge_sort([38,27,43,3,9,82,10])
merge_sort([38, 27, 43])
merge_sort([38]) 
merge_sort([27, 43])
merge_sort([27]) 
merge_sort([43])
merge_sort([3, 9, 82, 10])
merge_sort([3, 9])
merge_sort([3])
merge_sort([9])
merge_sort([82, 10])
merge_sort([82])
merge_sort([10])
merge_[3,9,10,82]
final_merge [3,9,10,27,38,43,82]
##
   
             
Exercise 1: Identify Time Complexity
For each of the following code snippets, determine its Time Complexity using
Big O Notation. Assume n is the size of the input array or list.

*linear_search → O(n)
Reason: Checks each element once in the list.
# linear_search(my_list, 6)
# linear_search(my_list, 100)
# Time Complexity: O(n)
# Reason: Checks each element until the target is found or the list ends → linear growth with n.

*Bubble Sort → O(n²)
Reason: Nested loops compare all pairs of elements.

# bubble_sort(list(my_list))
# Time Complexity: O(n²)
# Reason: Nested loops over the list → comparisons grow quadratically with n.

*Binary Search → O(log n)
Reason: List is halved at each step.

# binary_search(sorted_list, 7)
# binary_search(sorted_list, 100)
# Time Complexity: O(log n)
# Reason: Each step halves the search space → logarithmic growth with n.

*Merge Sort (Conceptual) → O(n log n)
Reason: List is split log n times, merging takes O(n) each.

# merge_sort_conceptual(list(my_list))
# Time Complexity: O(n log n)
# Reason: Recursively splits the list log n times, merging each segment takes O(n) → linearithmic growth.

*Fibonacci (Exponential) → O(2^n)
Reason: Recursive calls double at each level.

# fibonacci_exponential(5)
# fibonacci_exponential(10)
# Time Complexity: O(2^n)
# Reason: Recursive calls branch exponentially → double the work each level.

*Factorial Permutations (Conceptual) → O(n!)
Reason: Generates all possible permutations of n elements.

# factorial_permutations_conceptual(small_list)
# Time Complexity: O(n!)
# Reason: Generates all permutations of n elements → factorial growth.

| Algorithm              | Big O      | Reason                             |
| ---------------------- | ---------- | ---------------------------------- |
| Linear Search          | O(n)       | Checks each element once           |
| Bubble Sort            | O(n²)      | Nested loops over list             |
| Binary Search          | O(log n)   | List halved each step              |
| Merge Sort             | O(n log n) | Split log n times, merge each O(n) |
| Fibonacci (Recursive)  | O(2^n)     | Recursive calls double             |
| Factorial Permutations | O(n!)      | Generates all permutations         |


Exercise 2: Identify Space Complexity
For each of the following code snippets, determine its Space Complexity using
Big O Notation. Assume n is the size of the input array or list.

| Problem | Big O Notation |
| ------- | -------------- |
| 2.1     | O(1)           |
| 2.2     | O(n)           |
| 2.3     | O(n)           |


Exercise 3: Algorithm Comparison and Best Choice
Consider a scenario where you need to search for an element within a dataset of
N items.

# Sample Answer (You Can Write in Your Exercise Sheet)
# Comparison:
Linear search: O(N)
Binary search: O(log N) (requires sorted dataset)
Hash lookup: O(1) (requires extra memory)
# Best choice:
For a single search in a small unsorted dataset → Linear Search
For a large dataset that is sorted → Binary Search
For many repeated searches → Hash Table Lookup

Exercise 4: Real-World Scenario
Imagine you are building a social media application. One feature is to show a
user all posts made by their friends.

# Step 1: Identify the task
We have N friends
Each friend has M posts
Need to collect and display all posts

# Step 2: Consider possible approaches
Loop through friends and their posts → O(N × M)
Use a database query to fetch all posts in one go → O(1) to O(N) depending on indexing
for friend in friends:
    for post in friend.posts:
        show(post)

Time Complexity: O(N × M) → nested loops

Reason: For each of N friends, we look at M posts
Using a database query (optimized)
If posts are stored in a database, a query can return all posts in O(1) to O(N) depending on indexing
But in simple Python-style, nested loops → O(N × M)

# Step 3: Simple Answer You Can Write
Big O Notation: O(N × M)
# Reason (simple version):
You have to check all posts of all friends → grows with number of friends × posts per friend.
# ✅ Example Answer (1–2 lines for your sheet)
Time Complexity: O(N × M)
Reason: Must go through each friend and all of their posts to display them.