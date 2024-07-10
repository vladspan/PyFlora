import sqlite3

class BazaBilja:
    def __init__(self):
        self.bazaBiljaka = 'BazaBiljaka.db'
        self.query_create_table = '''CREATE TABLE IF NOT EXISTS Biljke
        (
            id INTEGER PRIMARY KEY,
            nazivBiljke TEXT UNIQUE,
            opis TEXT,
            nazivSlike TEXT
        )'''
        self.query_add = '''INSERT INTO Biljke (nazivBiljke, opis, nazivSlike) VALUES(?, ?, ?)'''
        self.query_select = '''SELECT nazivBiljke, opis, nazivSlike FROM Biljke'''
        self.createPlantTable()
    
    def createPlantTable(self):
        connection = None
        try:
            connection = sqlite3.connect(self.bazaBiljaka)
            cursor = connection.cursor()
            cursor.execute(self.query_create_table)
            connection.commit()
            cursor.close()
            print("Table 'Biljke' created or already exists.")
        except sqlite3.Error as e:
            print('Error creating database:', e)
        finally:
            if connection:
                connection.close()

    def dodavanjeBiljke(self, nazivBiljke, opis, nazivSlike):
        connection = None
        try:
            connection = sqlite3.connect(self.bazaBiljaka)
            cursor = connection.cursor()
            cursor.execute(self.query_add, (nazivBiljke, opis, nazivSlike))
            connection.commit()
            cursor.close()
            print(f'Plant {nazivBiljke} added successfully')  # Debug print
        except sqlite3.Error as e:
            print('Error adding plant:', e)
        finally:
            if connection:
                connection.close()

    def pretrazivanjeBiljke(self):
        plantData = []
        connection = None
        try:
            connection = sqlite3.connect(self.bazaBiljaka)
            cursor = connection.cursor()
            cursor.execute(self.query_select)
            plantData = cursor.fetchall()
            cursor.close()
            print('Plants fetched successfully:', plantData)  # Debug print
        except sqlite3.Error as e:
            print("Error fetching plants:", e)
        finally:
            if connection:
                connection.close()
        return plantData