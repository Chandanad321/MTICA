import sqlite3
carData=[
    (1,'Tani',10000),
    (2,'Jani',20000),
    (3,'Dani',30000),
    (4,'Nani',40000),
    (5,'rani',50000),
    (6,'Sani',60000),
    (7,'Pani',70000),
    (8,'Lani',80000),
    (9,'Mani',90000),
    ]
con=sqlite3.connect('mtica.db')
cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute("CREATE TABLE  Cars(Id INT, Name TEXT,Price INT)")

cur.executemany("INSERT INTO Cars VALUES(?,?,?)",carData)
con.commit()
con.close()
print("Values inserted.")









