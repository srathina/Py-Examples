import sqlite3 as s

# connection =  s.connect("family.db")

connection =  s.connect(":memory:")

cursor = connection.cursor()


cursor.execute("""CREATE TABLE family(
 	id INTEGER,
 	name TEXT)""")

cursor.execute("""INSERT INTO family values(
						1,
						"RSK")""")

cursor.execute("""INSERT INTO family values(
						2,
						"Anitha")""")

cursor.execute("""INSERT INTO family values(
						3,
						"Tanish")""")

# cursor.execute("UPDATE family SET name ='Jothi'")

cursor.execute("SELECT * FROM family WHERE name = 'RSK'") 
rows = cursor.fetchall()
for row in rows:
	print(row)


# cursor.execute("DELETE FROM family WHERE name is 'RSK'")

connection.commit()
connection.close()