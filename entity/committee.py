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