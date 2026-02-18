import sqlite3
# create sql db
conn = sqlite3.connect('employee.db') 
cur = conn.cursor()
# sql query to create tbl in db
cre_tbl = '''
    CREATE TABLE IF NOT EXISTS EMPLOYEE(
     id integer PRIMARY KEY AUTOINCREMENT,
     name text NOT NULL,
     position text NOT NULL,
     salary float NOT NULL
    )
''' 
cur.execute(cre_tbl)
print("creted tbl successfully")
conn.commit()
conn.close()