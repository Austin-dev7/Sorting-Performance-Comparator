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

import tkinter as tk
root = tk.Tk() 
root.title("Young Money App") 
root.geometry("400x300") 
root.mainloop()

# root=tk.Tk()
# root.title()
# import tkinter as tk

# def on_button_click():
#     print("button clicked!")
    
# # =tk.Trootk()
# button=tk.button(root,text="click me" , command=on_button_click) 
# button.pack()
# root.mainloop()
import tkinter as tk

def on_button_click():
    print("Button clicked!")

root = tk.Tk()
button = tk.Button(root, text="click me", command=on_button_click)
button.pack()
root.mainloop()











# root = tk.TK()

# root.title("Your App")

# lable = tk.Lable(root, text="Hello,Tkinter!")
# def on_button_click():
#     print("button click")
    
    
    
#     button = 
    
    
    




