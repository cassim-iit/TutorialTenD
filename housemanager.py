import sqlite3
def create_table() :
    con = sqlite3.connect('database\\house.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS house(houseID TEXT NOT NULL UNIQUE PRIMARY KEY, houseName TEXT NOT NULL)")
    con.commit()
    cur.close()
    con.close()

create_table()

