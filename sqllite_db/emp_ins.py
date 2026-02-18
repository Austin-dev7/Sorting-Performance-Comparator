import sqlite3

# create sql db
conn = sqlite3.connect('employee.db')
cur = conn.cursor()

# sql query to insert data in 
ins_tbl = '''
    INSERT INTO EMPLOYEE (name, position, salary) VALUES (?, ?, ?)
'''

data = [
     ('chris ', 'Food dept', 200.00),
    ('James', 'head of department', 56487.89),
     ('Ivan ', 'Admin department', 200.00),
    ('Jane', 'Tech department', 56487.89)
]

cur.executemany(ins_tbl, data)
print("Data inserted successfully")
conn.commit() 
