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

        # Create users table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        ''')

        # Create plants table if it doesn't exist
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
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            connection.commit()
            cursor.close()
            print(f'User {username} added successfully')
        except sqlite3.Error as e:
            print('Error adding user:', e)
        finally:
            connection.close()

    def provjeraKorisnika(self, username, password):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        return user

    def dodavanjeBiljke(self, ime, opis, slika):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute('INSERT INTO plants (username, plant_name, plant_description, plant_image) VALUES (?, ?, ?, ?)',
                       (self.userName, ime, opis, slika))
        connection.commit()
        cursor.close()

    def pretrazivanjeBiljke(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute('SELECT plant_name, plant_description, plant_image FROM plants WHERE username=?', (self.userName,))
        plants = cursor.fetchall()
        cursor.close()
        connection.close()
        return plants
    
    def dohvatiBiljkuImenom(self, name):
        self.cursor.execute('SELECT* FFROM plants WHERE naziv=?', (name, ))
        self.cursor.fetchone()

    def updateBiljke(self, plantId, naziv, opis, slika):
        self.cursor.execute('UPDATE plants SET naziv=?, opis=?, slika=? WHERE id=?',(plantId, naziv, opis, slika))
        self.connection.commit()

    def close(self):
        self.connection.close()

