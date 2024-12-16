from tkinter import *
from biljke_baza import BazaBilja
from tkinter import messagebox

class Biljka:
    def __init__(self, username):
        self.username = username
        self.baza = BazaBilja(self.username)

    def biljkaProzor(self, parent=None, plantData=None, refresh_callback=None):
        """Open a window to add or update a plant."""
        self.bazniOkvir = Toplevel(parent)
        self.bazniOkvir.geometry('400x400')
        self.bazniOkvir.title('Dodavanje/Updejtanje biljke')

        # Entry fields for plant data
        self.nazivBiljke = StringVar()
        self.opisBiljke = StringVar()
        self.imeFotografijeBiljke = StringVar()

        self.okvir = Frame(self.bazniOkvir)
        self.okvir.pack(pady=50)

        Label(self.okvir, text='Naziv biljke', font=('Helvetica', 14)).grid(row=0, column=0, pady=5)
        Entry(self.okvir, textvariable=self.nazivBiljke, width=30).grid(row=1, column=0, pady=5)

        Label(self.okvir, text='Opis biljke', font=('Helvetica', 14)).grid(row=2, column=0, pady=5)
        Entry(self.okvir, textvariable=self.opisBiljke, width=30).grid(row=3, column=0, pady=5)

        Label(self.okvir, text='Ime fotografije biljke', font=('Helvetica', 14)).grid(row=4, column=0, pady=5)
        Entry(self.okvir, textvariable=self.imeFotografijeBiljke, width=30).grid(row=5, column=0, pady=5)

        # Pre-fill fields for edit mode
        if plantData:
            self.nazivBiljke.set(plantData[2])
            self.opisBiljke.set(plantData[3])
            self.imeFotografijeBiljke.set(plantData[4])

        actionText = 'Updejtaj biljku' if plantData else 'Dodaj biljku'
        Button(
            self.okvir,
            text=actionText,
            command=lambda: self.unosBiljke(plantData, refresh_callback)
        ).grid(row=6, column=0, pady=10)

    def unosBiljke(self, plantData=None, refresh_callback=None):
        """Add or update plant in the database."""
        naziv = self.nazivBiljke.get()
        opis = self.opisBiljke.get()
        slika = self.imeFotografijeBiljke.get()

        if not naziv or not opis or not slika:
            messagebox.showerror('Error', 'All fields are required')
            return

        if plantData:
            # Update plant
            self.baza.updateBiljke(plantData[0], naziv, opis, slika)
        else:
            # Add new plant
            self.baza.dodavanjeBiljke(naziv, opis, slika)

        if refresh_callback:
            refresh_callback()

        self.bazniOkvir.destroy()
