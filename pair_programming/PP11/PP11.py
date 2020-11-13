##collaborators: Mark Penrod, Connor Francis Capitolo, Boer Zhang
import sqlite3

db = sqlite3.connect('PP11.sqlite')
cursor = db.cursor()

with open('candidates.txt','r') as f:
    content = f.readlines()

content = [x.strip() for x in content] 
content
cursor.execute("DROP TABLE IF EXISTS candidates")
cursor.execute('''CREATE TABLE candidates (
               id INTEGER PRIMARY KEY NOT NULL, 
               first_name TEXT, 
               last_name TEXT, 
               middle_init TEXT, 
               party TEXT NOT NULL)''')
for item in content[1:]:
    cursor.execute('''INSERT INTO candidates
                (id, first_name, last_name, middle_init, party)
                VALUES (?, ?, ?, ?, ?)''', 
                    tuple(item.split('|')))

db.commit()
db.close()