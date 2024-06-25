import sqlite3
import os

class Baza:       
    def __init__(self):
        self.database = 'BazaKorisnika.db'
        self.query = '''CREATE TABLE IF NOT EXISTS Korisnici
        (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT 
            )
            '''
        self.query_add = '''INSERT INTO Korisnici
                (username, password)
                VALUES(?, ?)
                '''
        
    def kreiranjeBaze(self):          
            try:
                connection = sqlite3.connect(self.database)
                cursor = connection.cursor()

                cursor.execute(self.query)
                connection.commit()

                cursor.close()
        
            except sqlite3.Error as e:
                print('Dogodila se greška', e)
            
            finally:
                connection.close()
        
    def dodavanjeKorisnika(self, username, password):           
            try: 
                connection = sqlite3.connect(self.database)
                cursor = connection.cursor()

                cursor.execute(self.query_add, (username, password))
                connection.commit()
                          
                cursor.close()

            except sqlite3.Error as e:
                print('Dogodila se greška prilikom dodavanja korisnika', e)

            finally:
                connection.close()
        
    def noviKorisnik(self, username, password):
        if not os.path.exists(self.database):
            self.kreiranjeBaze()
            self.dodavanjeKorisnika(username, password)
        
        else:
            self.dodavanjeKorisnika(username, password)
                     