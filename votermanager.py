import sqlite3 as db
from entity.voter import voter

def initializeDatabase():
    sql = "CREATE TABLE IF NOT EXISTS voter(iitnumber TEXT PRIMARY KEY, name TEXT,district TEXT,nic TEXT ,age TEXT)"
    con = db.connect("database\\voter.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    cur.close()
    con.close()

initializeDatabase()
