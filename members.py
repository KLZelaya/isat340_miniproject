import sqlite3
conn = sqlite3.connect("celebrity.db")
cursor = conn.cursor()

sql = "create table celebs (celebsID integer PRIMARY KEY, firstname text, lastname text, age int, email text, " \
      "photo text, bio text)"

table2 = "create table members (memberID integer PRIMARY KEY, firstname text, lastname text, age int, email text, " \
         "bio text)"

cursor.execute(sql)
cursor.execute(table2)

conn.commit()
conn.close()