#import the built-in sqlite3
import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()


#--------------MAKING THE TABLES------------------

sql = "create table celebs (celebsID integer PRIMARY KEY, firstname text, lastname text, age int, email text, " \
      "photo text, bio text)"

table2 = "create table members (memberID integer PRIMARY KEY, firstname text, lastname text, age int, email text, " \
         "bio text, username, password)"

cursor.execute(sql)
cursor.execute(table2)

#------------INSERTING THE INFORMATIION-------------

insert = "insert into celebs values (?, ?, ?, ?, ?, ?, ?)"
data = ( (1, "Angelina", "Jolie", 40, "angie@hollywood.us", "http://www.nphinity.com/pics/aj.jpg", "I was born in LA."),
         (2, "Brad", "Pitt", 51, "brad@hollywood.us", "http://www.nphinity.com/pics/bp.jpg", "I was born in Oklahoma" ),
         (3, "Snow", "White", 21, "sw@disney.org", "http://www.nphinity.com/pics/sw.jpg", "I'm a princess"),
         (4, "Darth", "Vader", 29, "dv@darkside.me", "http://www.nphinity.com/pics/dv.jpg", "I am your father"),
         (5, "Taylor", "Swift", 25, "ts@1989.us", "http://www.nphinity.com/pics/ts.jpg", "I'm an artist"),
         (6, "Beyonce", "Knowles", 34, "beyonce@jayze.me", "http://www.nphinity.com/pics/bk.jpg", "I have three kids"),
         (7, "Selena", "Gomez", 23, "selena@hollywood.us", "http://www.nphinity.com/pics/sg.jpg", "I used to work at "
                                                                                                  "disney"),
         (8, "Stephen", "Curry", 27, "steph@golden.bb", "http://www.nphinity.com/pics/sc.jpg", "I am a basketball " ""
                                                                                               "player"))

cursor.executemany(insert, data)

insertMembers = "insert into members values (?, ?, ?, ?, ?, ?, ?, ?)"
dataMembers = ((1, "Kelly", "Lopez Zelaya", 20, "lopezzkn@dukes.jmu.edu", "I was born in New York City...", "lopez", "hello"),
               (2, "Spencer", "Garrett", 20, "garre2sd@dukes.jmu.edu", "I was born in Sterling", "garrett", "goodbye"))

cursor.executemany(insertMembers, dataMembers)

conn.commit()

#----------RETRIEVING THE DATA--------------

retrieveCelebs = "select * from celebs"
cursor.execute(retrieveCelebs)
rows = cursor.fetchall()

for row in rows:
    print(row)


retrieveMembers = "select * from members"
cursor.execute(retrieveMembers)
rowsMembers = cursor.fetchall()

for row in rowsMembers:
    print(row)


conn.close()
