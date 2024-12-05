
import sqlite3
def create_table() :
    con = sqlite3.connect('database\\house.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS house(houseID TEXT NOT NULL UNIQUE PRIMARY KEY, houseName TEXT NOT NULL)")
    con.commit()
    cur.close()
    con.close()
def create_house():
    pass
def update_house():
    pass
def remove_house():
    pass

def menu():
    x = 0
    while x != 9:
        print("1: Create a house")
        print("2: Update a house")
        print("3: Remove a house")
        print("9: Exit")
        try:
            x= int(input("Enter your choice: "))
        except ValueError:
            pass
        else:
            match x:
                case 1:
                    create_house()
                case 2:
                    update_house()
                case 3:
                    remove_house()
                case  9 :
                    print("Thank you!")
                    pass
                case _ :
                    print("Invalid choice")
create_table()
menu()



import sqlite3
def create_table() :
    con = sqlite3.connect('database\\house.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS house(houseID TEXT NOT NULL UNIQUE PRIMARY KEY, houseName TEXT NOT NULL)")
    con.commit()
    cur.close()
    con.close()

create_table()

