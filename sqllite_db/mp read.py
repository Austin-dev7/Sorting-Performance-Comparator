import sqlite3
# create sql db
conn = sqlite3.connect('employee.db') 
cur = conn.cursor()
# sql query to create tbl in db
cre_tbl = '''
    SELECT * FROM employee 
''' 
cur.execute(cre_tbl)
print("Reading tbl successfully")
rows = cur.fetchall()
for row in rows:
    print(row)
conn.commit()
conn.close()