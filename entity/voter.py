import sqlite3 as db

class voter:
    def _init_(self, iitnumber = "",name ="",  district = "",nic="",age=""):
        self.age = age
        self.nic = nic
        self.district = district
        self.name = name
        self.iitnumber = iitnumber

    def load(self):
        sql = "SELECT age,nic,district,name FROM voter WHERE iitnumber = ?"
        con = db.connect("database\\login.db")
        cur = con.cursor()
        cur.execute(sql, (self.iitnumber,))
        row = cur.fetchone()
        cur.close()
        con.close()
        self.iitnumber= row[0]
        self.name = row[1]
        self.nic = row[2]
        self.age = row[3]
        self.district = row[4]
        return True




    def update_table(self):
        sql = "UPDATE user SET name = ?, district = ?, nic = ?, age = ?  WHERE iitnumber = ?"
        con = db.connect("database\\login.db")
        cur = con.cursor()
        cur.execute(sql, (self.name, self.district, self.nic, self.age))
        con.commit()
        cur.close()
        con.close()
        return True