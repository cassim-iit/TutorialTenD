import sqlite3 as db

class voter:
    def _init_(self, iitnumber = "",name ="",  district = "",nic="",age=""):
        self.age = age
        self.nic = nic
        self.district = district
        self.name = name
        self.iitnumber = iitnumber

    def load(self):
        sql = "SELECT name,age,nic,district FROM user WHERE userName = ?"
        con = db.connect("database\\voter.db")
        cur = con.cursor()
        cur.execute(sql, (self.username,))
        row = cur.fetchone()
        cur.close()
        con.close()
        self.iitnumber = row[0]
        self.name= row[1]
        self.age= row[2]
        self.nic= row[3]
        self.district= row[4]
        return True

    def update(self):
        sql = "UPDATE voter SET name = ?,age=?,nic=?,district=? WHERE iitnumber = ?"
        con = db.connect("database\\voter.db")
        cur = con.cursor()
        cur.execute(sql, (self.name, self.age,self.nic,self.district))
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
        return True

    def delete(self):
        sql = "DELETE FROM voter WHERE iitnumber = ?"
        con = db.connect("database\\voter.db")
        cur = con.cursor()
        cur.execute(sql, (self.iitnumber,))
        con.commit()
        cur.close()
        con.close()
        return True