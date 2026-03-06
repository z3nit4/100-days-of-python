# DATABASES

import sqlite3

connection = sqlite3.connect('mydata.db') # Returns a connection to database
cursor = connection.cursor() # Cursor is the database's interface

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    email VARCHAR(32),
    password_hash TEXT,
    user_id INTEGER PRIMARY KEY
)
""") # Execute is the method used to execute a query

users = [ 
    ('strongjohn', 'johnstrong@gmail.com', 'JohnSoStrong123', 556),
    ('lisa28', 'lisa.m@outlook.com', 'LisaM@1995', 275),
    ('johndoe', 'johndoe@userenterprises.com', 'JohnDoe', 423)
]

cursor.executemany("INSERT INTO users VALUES (?,?,?,?)", users) # ? are placeholders which prevents SQL injection and is standard practice.

cursor.execute("SELECT * FROM users")

rows = cursor.fetchall()
print(rows)

# To commit anything to database we use:
connection.commit()
connection.close()