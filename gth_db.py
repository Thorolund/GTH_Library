import sqlite3

con = sqlite3.connect("Library_db.db")
curs = con.cursor()
#start code

def create():
    curs.execute("""CREATE TABLE IF NOT EXISTS reader (
                 id INTEGER PRIMARY KEY
                 pr TEXT PRIMARY KEY
                 full_name TEXT NOT NULL
                 phone TEXT NOT NULL
                age INTEGER NOT NULL
    )""")
test
con.commit()