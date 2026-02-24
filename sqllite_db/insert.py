import sqlite3

# create sql db
conn = sqlite3.connect('data.db')
cur = conn.cursor()

# sql query to insert data in 
ins_tbl = '''
    INSERT INTO USER (name, age, email) VALUES (?, ?, ?)
'''

name = input("Enter name: ")
age = int(input("Enter age: "))
email = input("Enter email: ")

data = [
     (name, age, email)
   
   
]
cur.executemany(ins_tbl, data)
print("Data inserted successfully")
conn.commit()  
conn.close() 
