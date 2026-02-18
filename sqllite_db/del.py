import sqlite3
# create sql db
conn = sqlite3.connect('data.db') 
cur = conn.cursor()
# sql query to create tbl in db
cre_tbl = '''
    DELETE FROM user WHERE id = 6
    
''' 

cur.execute(cre_tbl)
print("Deleting user successfully")

conn.commit()
conn.close()