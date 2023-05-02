import sqlite3

conn = sqlite3.connect("../02-context-managers/tp/ma_base.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
cursor.execute("INSERT INTO users(name, age) VALUES (?,?)", ("DUPONT", 43))
conn.commit()
cursor.execute("SELECT * FROM users")
for line in cursor.fetchall():
    print(line)

cursor.close()
conn.close()