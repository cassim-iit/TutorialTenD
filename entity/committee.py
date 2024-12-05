import sqlite3 as db
from math import trunc

class Committee:
    def __init__(self, committee = "",  id = ""):
        self.committee = committee
        self.id = id