# DATABASES with OOP

import sqlite3

class User:

    def __init__(self, username, email, password_hash, user_id):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.user_id = user_id
        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor()


    def load_user(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        results = self.cursor.fetchone()

        if results:
            self.username = results[0]
            self.email = results[1]
            self.password_hash = results[2]
            self.user_id = results[3]
    
    def insert_user(self):
        self.cursor.execute("INSERT INTO users VALUES (?,?,?,?)", (self.username, self.email, self.password_hash, self.user_id))

        self.connection.commit()

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()

u1 = User('tracymcgrady', 'tmac@nba.com', 'NeedaRing123', 25)
u1.load_user(25)
print(u1.username)
print(u1.email)
print(u1.password_hash)
print(u1.user_id)

u2 = User('robg', 'rob49@record.com', '12345678', 47)
u2.insert_user()

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM users")
results = cursor.fetchall()
print(results)
connection.close()