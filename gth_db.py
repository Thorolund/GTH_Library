import sqlite3

con = sqlite3.connect("Library_db.db")
curs = con.cursor()
#start code

con.commit()