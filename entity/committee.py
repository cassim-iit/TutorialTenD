import sqlite3 as db
from math import trunc

class Committee:
    def __init__(self, committee = "",  id = ""):
        self.committee = committee
        self.id = id

    def save(self):
        sql = "INSERT INTO committee (committee, id) VALUES (?, ?)"
        con = db.connect("database\\committee.db")
        cur = con.cursor()
        cur.execute(sql, (self.committee, self.id))
        con.commit()
        cur.close()
        con.close()

    def load(self):
        sql = "SELECT committee,id FROM committee WHERE committee = ?"
        con = db.connect("database\\committee.db")
        cur = con.cursor()
        cur.execute(sql, (self.committee,))
        row = cur.fetchone()
        cur.close()
        con.close()
        self.committee = row[0]
        self.id = row[1]
        return True