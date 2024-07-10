from tkinter import*
from biljke_baza import BazaBilja

class Biljka:
    def biljkaProzor(self, parent):
        self.bazniOkvir = Toplevel(parent)
        self.bazniOkvir.geometry('400x400')
        self.bazniOkvir.title('PyPosuda - dodavanje biljke')

        self.nazivBiljke = StringVar()
        self.opisBiljke = StringVar()
        self.imeFotografijeBiljke = StringVar()

        self.okvir = Frame(self.bazniOkvir)
        self.okvir.pack(pady=50)

        self.oznakaIme = Label(self.okvir, text='Naziv biljke', foreground='orange', font=('Helvetica', 20, 'normal', 'roman'))
        self.oznakaIme.grid(row=0, column=0)

        self.unosoznakaIme = Entry(self.okvir, textvariable=self.nazivBiljke)
        self.unosoznakaIme.grid(ipadx=40, row=1, column=0)

        self.oznakaOpis = Label(self.okvir, text='Opis biljke', foreground='orange', font=('Helvetica', 20, 'normal', 'roman'))
        self.oznakaOpis.grid(row=2, column=0)

        self.unosoznakaOpis = Entry(self.okvir, textvariable=self.opisBiljke)
        self.unosoznakaOpis.grid(ipadx=40, row=3, column=0)

        self.oznakaFotografijaIme = Label(self.okvir, text='Ime fotografije biljke', foreground='orange', font=('Helvetica', 20, 'normal', 'roman'))
        self.oznakaFotografijaIme.grid(row=4, column=0)

        self.unosImeFotografije = Entry(self.okvir, textvariable=self.imeFotografijeBiljke)
        self.unosImeFotografije.grid(ipadx=40, row=5, column=0)

        self.dodajBiljku = Button(self.okvir, text='Dodaj biljku', command=self.unosBiljke)
        self.dodajBiljku.grid(row=6, column=0)

        self.errorMessage = Label(self.okvir, text='', foreground='red', font=('Helvetica', 12, 'normal', 'roman'))
        self.errorMessage.grid(row=7, columnspan=2, pady=10)
    
    def unosBiljke(self):
        imeBiljke = self.nazivBiljke.get()
        karakteristikeBiljke = self.opisBiljke.get()
        fotkaImeBiljke = self.imeFotografijeBiljke.get()

        if not imeBiljke or not karakteristikeBiljke or not fotkaImeBiljke:
            self.errorMessage.config(text='Error: All fields are required')
            self.errorMessage.after(3000, lambda: self.errorMessage.config(text=''))
        else:
            try:
                fotkaBiljke = PhotoImage(file=fotkaImeBiljke)
                self.oznakaFotografija = Label(self.okvir, image=fotkaBiljke)
                self.oznakaFotografija.image = fotkaBiljke  # Keep a reference to avoid garbage collection
                self.oznakaFotografija.grid(row=8, column=0, pady=10)
                
                BazaBilja().dodavanjeBiljke(imeBiljke, karakteristikeBiljke, fotkaImeBiljke)
                self.errorMessage.config(text='Plant added successfully', foreground='green')
                self.errorMessage.after(3000, lambda: self.errorMessage.config(text=''))
                self.bazniOkvir.destroy()
            except Exception as e:
                self.errorMessage.config(text=f'Error: {e}')
                self.errorMessage.after(3000, lambda: self.errorMessage.config(text=''))

if __name__ == '__main__':
    Biljka()