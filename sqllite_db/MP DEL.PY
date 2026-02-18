import sqlite3
# create sql db
conn = sqlite3.connect('EMPLOYEE.db') 
cur = conn.cursor()
# sql query to create tbl in db
cre_tbl = '''
    DELETE FROM EMPLOYEE WHERE id = 1
    
''' 

cur.execute(cre_tbl)
print("Deleting EMPLOYEE successfully")

conn.commit()
conn.close()