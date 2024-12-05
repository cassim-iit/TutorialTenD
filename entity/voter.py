import sqlite3 as db

class voter:
    def _init_(self, iitnumber = "",name ="",  district = "",nic="",age=""):
        self.age = age
        self.nic = nic
        self.district = district
        self.name = name
        self.iitnumber = iitnumber

    def update_table(self):
        sql = "UPDATE user SET name = ?, district = ?, nic = ?, age = ?  WHERE iitnumber = ?"
        con = db.connect("database\\login.db")
        cur = con.cursor()
        cur.execute(sql, (self.name, self.district, self.nic, self.age))
        con.commit()
        cur.close()
        con.close()
        return True

    def save(self):
        sql = "INSERT INTO voter (age, nic, district, name, iitnumber) VALUES (?, ?)"
        con = db.connect("database\\login.db")
        cur = con.cursor()
        cur.execute(sql, (self.age, self.nic, self.district, self.name, self.iitnumber))
        con.commit()
        cur.close()
        con.close()