import sqlite3 as db
from math import trunc

class Committee:
    def __init__(self, committee_id = "",  committee_name = ""):
        self.committeeid = committee_id
        self.committeename = committee_name

    def save(self):
        sql = "INSERT INTO committee (committeeID, committeeName) VALUES (?, ?)"
        con = db.connect("database\\committee.db")
        cur = con.cursor()
        cur.execute(sql, (self.committeeid, self.committeename))
        con.commit()
        cur.close()
        con.close()

    def load(self):
        sql = "SELECT committeeID,committeeName FROM committee WHERE committeeName = ?"
        con = db.connect("database\\committee.db")
        cur = con.cursor()
        cur.execute(sql, (self.committeename,))
        row = cur.fetchone()
        cur.close()
        con.close()
        self.committeeid = row[0]
        self.committeename = row[1]
        return True

    def delete(self):
        sql = "DELETE FROM committee WHERE committeeID = ?"
        con = db.connect("database\\login.db")
        cur = con.cursor()
        cur.execute(sql, (self.committeeid,))
        con.commit()
        cur.close()
        con.close()
        return True

    def update(self):
        sql = "UPDATE committee SET committeeName = ? WHERE committeeID = ?"
        con = db.connect("database\\login.db")
        cur = con.cursor()
        cur.execute(sql, (self.committeename, self.committeeid))
        con.commit()
        cur.close()
        con.close()
        return True