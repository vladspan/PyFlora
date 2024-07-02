import sqlite3
class Baza:
    def __init__(self):
        self.database = 'BazaKorisnika.db'
        self.query_create_table = '''CREATE TABLE IF NOT EXISTS Korisnici
        (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT 
        )'''
        self.query_add = '''INSERT INTO Korisnici (username, password) VALUES(?, ?)'''
        self.query_select = '''SELECT username, password FROM Korisnici'''
        self.createTable()

    def createTable(self):
        try:
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()
            cursor.execute(self.query_create_table)
            connection.commit()
            cursor.close()
            print("Table 'Korisnici' created or already exists.")
        except sqlite3.Error as e:
            print('Error creating database:', e)
        finally:
            connection.close()

    def dodavanjeKorisnika(self, username, password):
        try:
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()
            cursor.execute(self.query_add, (username, password))
            connection.commit()
            cursor.close()
            print(f'User {username} added successfully')  # Debug print
        except sqlite3.Error as e:
            print('Error adding user:', e)
        finally:
            connection.close()

    def pretrazivanjeKorisnika(self):
        userNameData = []
        try:
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()
            cursor.execute(self.query_select)
            userNameData = cursor.fetchall()
            cursor.close()
            print('Users fetched successfully:', userNameData)  # Debug print
        except sqlite3.Error as e:
            print("Error fetching users:", e)
        finally:
            connection.close()
        return userNameData