import sqlite3
# create sql db
conn = sqlite3.connect('employee.db') 
cur = conn.cursor()
# sql query to create tbl in db
cre_tbl = '''
    UPDATE EMPLOYEE SET name = ? WHERE id = ?
    
''' 
par = ('MICHEAL', 2)

cur.execute(cre_tbl, par)
print("Updating tbl successfully")

conn.commit()
conn.close()
