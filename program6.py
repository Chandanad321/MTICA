import sqlite3 as lite
con = lite.connect('mtica.db')

cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute('''CREATE TABLE  Cars(
        Id INT, Name TEXT,Price INT)''')
print("table cars cereated.")
cur.execute("INSERT INTO Cars VALUES(1,'Rani',52642)")
cur.execute("INSERT INTO Cars VALUES(2,'Soni',57127)")

cur.execute("INSERT INTO Cars VALUES(3,'Tani',9000)")
cur.execute("INSERT INTO Cars VALUES(4,'Vani',29000)")
cur.execute("INSERT INTO Cars VALUES(5,'Pani',35000)")
cur.execute("INSERT INTO Cars VALUES(6,'Nani',40000)")
cur.execute("INSERT INTO Cars VALUES(7,'Yani',52000)")
cur.execute("INSERT INTO Cars VALUES(8,'Kani',63000)")

con.commit()
print("Values in tables car inserted.")









