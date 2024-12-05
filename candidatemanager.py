import sqlite3
import entity.candidate

def create_table() :
    sql = "CREATE TABLE IF NOT EXISTS candidate(candidateID TEXT NOT NULL UNIQUE PRIMARY KEY, candidateName TEXT NOT NULL, candidateAge INT NOT NULL, gender TEXT NOT NULL)"
    con = sqlite3.connect('database\\candidates.db')
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()

create_table()

def insertUser(candidateID, candidateName,candidateAge,gender):
    oUser =  User()
    oUser.candidateID = candidateID
    oUser.candidateName = candidateName
    oUser.gender = gender
    oUser.save()

def removeUser(userName):
    oUser = candidate()
    oUser.candidateName = userName
    oUser.delete()

    #ADAREI HAMOTAMA UMMA KATE