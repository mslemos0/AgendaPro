import sqlite3
import hashlib
import customtkinter as ctk

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
            
            """)

username1, password1, = "mike123", hashlib.sha256("mikepassword".encode()).hexdigest()
username2, password2, = "Joao", hashlib.sha256("joao1234".encode()).hexdigest()
username3, password3, = "Matheus", hashlib.sha256("sense9842".encode()).hexdigest()
username4, password4, = "Giovanna", hashlib.sha256("giovannaegger4".encode()).hexdigest()

cur.execute("INSERT INTO userdata(username, password) VALUES (?,?)", (username1,password1))
cur.execute("INSERT INTO userdata(username, password) VALUES (?,?)", (username2,password2))
cur.execute("INSERT INTO userdata(username, password) VALUES (?,?)", (username3,password3))
cur.execute("INSERT INTO userdata(username, password) VALUES (?,?)", (username4,password4))

conn.commit()