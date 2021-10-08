import sqlite3
import os

file_exists = True
if not os.path.isfile('downloaded_files.db'):
    file_exists = False

conn = sqlite3.connect('downloaded_files.db')
c = conn.cursor()
if not file_exists:
    c.execute("""CREATE TABLE files (
                path text
                )""")
    print("OK")
c. execute("INSERT INTO files VALUES ('hallo')")

c.execute("SELECT * FROM files WHERE path='hallo'")
print(c.fetchall())
conn.commit()
conn.close()