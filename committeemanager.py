import sqlite3 as db
from entity.committee import Committee


def initializeDatabase():
    sql = "CREATE TABLE IF NOT EXISTS committee(commetteeID INT PRIMARY KEY, committeeName  TEXT )"
    con = db.connect("database\\committee.db")
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    cur.close()
    con.close()

def insertCommittee(committeeID, committeeName):
    oCommittee = Committee()
    oCommittee.committeeid = committeeID
    oCommittee.committeename = committeeName
    oCommittee.save()

def removeCommittee(committeeID):
    oCommittee = Committee()
    oCommittee.committeeid = committeeID
    oCommittee.delete()

def updateCommittee(committeeID, committeeName):
    oCommittee = Committee()
    oCommittee.committeeid = committeeID
    oCommittee.committeename = committeeName
    oCommittee.update()

def getCommittee(committeeName):
    oCommittee = Committee()
    oCommittee.committeename = committeeName
    oCommittee.load()
    return oCommittee

def getAllCommittees():
    oCommittees = []
    sql = "SELECT committeeID, committeeName FROM committee"
    con = db.connect("database\\committee.db")
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()
    con.close()
    for row in rows:
        oCommittee = Committee()
        oCommittee.committeeid = row[0]
        oCommittee.committeename = row[1]
        oCommittees.append(oCommittee)
    return oCommittees

def printCommitteeList(oCommittees):
    for oCommittee in oCommittees:
        print(oCommittee.committeeid, oCommittee.committeename)

def menu():
    x = 0;
    while (x != 9):
        print("1. Show all committees\n"
              "2. Add new committee\n"
              "3. Remove committee\n"
              "4. Update committee\n"
              "9. Exit")
        x = int(input("Enter your choice: "))
        match x:
            case 1:
                oList = getAllCommittees()
                printCommitteeList(oList)
            case 2:
                committeeID = input("Enter new committee id: ")
                committeeName = input("Enter new committee name: ")
                insertCommittee(committeeID,committeeName)
                print("Committee added successfully")
            case 3:
                committeeID = input("Enter committee id: ")
                removeCommittee(committeeID)
                print("Committee removed successfully")
            case 4:
                committeeID = input("Enter committee id: ")
                committeeName = input("Enter committee name: ")
                updateCommittee(committeeID,committeeName)
                print("Committee updated successfully")

#main for this module
initializeDatabase()
menu()




