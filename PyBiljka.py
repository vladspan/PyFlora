from tkinter import *
from biljke_baza import BazaBilja

class Biljka:
    def __init__(self, username):
        self.username = username
        self.baza = BazaBilja(username)

    def biljkaProzor(self, parent):
        self.bazniOkvir = Toplevel(parent)
        self.bazniOkvir.geometry('400x400')
        self.bazniOkvir.title('PyPosuda - dodavanje biljke')

        self.nazivBiljke = StringVar()
        self.opisBiljke = StringVar()
        self.imeFotografijeBiljke = StringVar()

        self.okvir = Frame(self.bazniOkvir)
        self.okvir.pack(pady=50)

        self.oznakaIme = Label(self.okvir, text='Naziv biljke', foreground='orange', font=('Helvetica', 20))
        self.oznakaIme.grid(row=0, column=0)

        self.unosoznakaIme = Entry(self.okvir, textvariable=self.nazivBiljke)
        self.unosoznakaIme.grid(ipadx=40, row=1, column=0)

        self.oznakaOpis = Label(self.okvir, text='Opis biljke', foreground='orange', font=('Helvetica', 20))
        self.oznakaOpis.grid(row=2, column=0)

        self.unosoznakaOpis = Entry(self.okvir, textvariable=self.opisBiljke)
        self.unosoznakaOpis.grid(ipadx=40, row=3, column=0)

        self.oznakaFotografijaIme = Label(self.okvir, text='Ime fotografije biljke', foreground='orange', font=('Helvetica', 20))
        self.oznakaFotografijaIme.grid(row=4, column=0)

        self.unosImeFotografije = Entry(self.okvir, textvariable=self.imeFotografijeBiljke)
        self.unosImeFotografije.grid(ipadx=40, row=5, column=0)

        self.dodajBiljku = Button(self.okvir, text='Dodaj biljku', command=self.unosBiljke)
        self.dodajBiljku.grid(row=6, column=0)

        self.errorMessage = Label(self.okvir, text='', foreground='red', font=('Helvetica', 12))
        self.errorMessage.grid(row=7, columnspan=2, pady=10)

    def unosBiljke(self):
        imeBiljke = self.nazivBiljke.get()
        karakteristikeBiljke = self.opisBiljke.get()
        fotkaImeBiljke = self.imeFotografijeBiljke.get()

        if not imeBiljke or not karakteristikeBiljke or not fotkaImeBiljke:
            self.errorMessage.config(text='Error: All fields are required')
            self.errorMessage.after(3000, lambda: self.errorMessage.config(text=''))
            return

        self.baza.dodavanjeBiljke(imeBiljke, karakteristikeBiljke, fotkaImeBiljke)
        self.bazniOkvir.destroy()
