import sqlite3 as db
from math import trunc

class Committee:
    def __init__(self, committeename = "",  id = ""):
        self.committeename = committeename
        self.id = id

    def save(self):
        sql = "INSERT INTO committee (committeeName, iD) VALUES (?, ?)"
        con = db.connect("database\\committee.db")
        cur = con.cursor()
        cur.execute(sql, (self.committeename, self.id))
        con.commit()
        cur.close()
        con.close()

    def load(self):
        sql = "SELECT committeeName,iD FROM committee WHERE committeeName = ?"
        con = db.connect("database\\committee.db")
        cur = con.cursor()
        cur.execute(sql, (self.committeename,))
        row = cur.fetchone()
        cur.close()
        con.close()
        self.committeename = row[0]
        self.id = row[1]
        return True