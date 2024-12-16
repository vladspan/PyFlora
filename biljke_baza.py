from tkinter import *
from tkinter import messagebox
import sqlite3


class BazaBilja:
    def __init__(self, userName):
        self.userName = userName
        self.database = 'plants.db'
        self.createTables()
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    def createTables(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        ''')

        # Create plants table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS plants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                plant_name TEXT,
                plant_description TEXT,
                plant_image TEXT,
                FOREIGN KEY(username) REFERENCES users(username)
            )
        ''')
        connection.commit()
        cursor.close()

    def dodavanjeKorisnika(self, username, password):
        try:
            self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            self.connection.commit()
        except sqlite3.Error as e:
            print('Error adding user:', e)

    def provjeraKorisnika(self, username, password):
        self.cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        return self.cursor.fetchone()

    def dodavanjeBiljke(self, ime, opis, slika):
        self.cursor.execute(
            'INSERT INTO plants (username, plant_name, plant_description, plant_image) VALUES (?, ?, ?, ?)',
            (self.userName, ime, opis, slika)
        )
        self.connection.commit()

    def pretrazivanjeBiljke(self):
        self.cursor.execute("SELECT * FROM plants WHERE username=?", (self.userName,))
        return self.cursor.fetchall()

    def updateBiljke(self, plantId, naziv, opis, slika):
        self.cursor.execute(
            'UPDATE plants SET plant_name=?, plant_description=?, plant_image=? WHERE id=?',
            (naziv, opis, slika, plantId)
        )
        self.connection.commit()

    def close(self):
        self.connection.close()


