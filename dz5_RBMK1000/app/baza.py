import sqlite3
connect=sqlite3.connect("banko.db")
cursor=connect.cursor()
def kudbuhon():
   
    cursor.execute("""CREATE TABLE IF NOT EXISTS clients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        balanse INTEGER DEFAULT NULL
    )
    """)
    cursor.execute(f"INSERT INTO clients (name,balanse) VALUE(?,?)")







    