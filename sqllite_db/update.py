import sqlite3
# create sql db
conn = sqlite3.connect('data.db') 
cur = conn.cursor()
# sql query to create tbl in db
cre_tbl = '''
    UPDATE user SET age = ? WHERE id = ?
    
''' 
par = (27, 2)

cur.execute(cre_tbl, par)
print("Updating tbl successfully")

conn.commit()
conn.close()