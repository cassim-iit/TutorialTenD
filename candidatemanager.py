import sqlite3
def create_table() :
    con = sqlite3.connect('database\\candidates.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS candidate(candidateID TEXT NOT NULL UNIQUE PRIMARY KEY, candidateName TEXT NOT NULL, candidateAge INT NOT NULL, gender TEXT NOT NULL)")
    con.commit()
    con.close()

create_table()