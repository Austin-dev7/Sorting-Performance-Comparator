import sqlite3

# create sql db
conn = sqlite3.connect('data.db')
cur = conn.cursor()

# sql query to create tbl in db
cre_tbl = '''
    CREATE TABLE IF NOT EXISTS USER(
     id integer PRIMARY KEY AUTOINCREMENT,
     name text NOT NULL,
     age integer NOT NULL,
     email text UNIQUE NOT NULL
    )
'''

cur.execute(cre_tbl)


print("Table created successfully")
conn.commit()
conn.close() 

