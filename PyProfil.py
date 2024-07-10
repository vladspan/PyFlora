from tkinter import *
from biljke_baza import *
from PyBiljka import Biljka

class PyProfil():
    def __init__(self):
        
        self.bazniDio = Tk()
        self.bazniDio.geometry('800x800')
        self.okvirniDio = Frame(self.bazniDio)
        self.okvirniDio.pack(pady=50)
        
        plantData = BazaBilja().pretrazivanjeBiljke()

        rowP = 0

        for biljka in plantData:
            self.scr(rowP, biljka)
            rowP += 2  # Each plant takes two rows

        self.addButton = Button(self.bazniDio, text='+', command=self.dodavanjeBiljke)
        self.addButton.pack(ipadx=20, ipady=20)
            
        self.bazniDio.mainloop()

    def dodavanjeBiljke(self):
        Biljka().biljkaProzor(self.bazniDio)

    def scr(self, r, p):
        name_label = Label(self.okvirniDio, text=f'{p[0]}', foreground="grey", 
              background="orange", borderwidth=2, relief="groove", 
              padx=10, pady=10, anchor="center")
        name_label.grid(row=r, column=0, columnspan=1, sticky="nsew")
        
        description_label = Label(self.okvirniDio, text=f'{p[1]}')
        description_label.grid(row=r+1, column=0, columnspan=1, sticky="nsew")

        spacer_label = Label(self.okvirniDio, text='')
        spacer_label.grid(column=1, columnspan=2, rowspan=2)
        
        self.fotka = PhotoImage(file=p[2])
        image_label = Label(self.okvirniDio, image=self.fotka)
        image_label.image = self.fotka  # Keep a reference to avoid garbage collection
        image_label.grid(row=r, column=3, rowspan=2, sticky="nsew")

        height_spacer = Label(self.okvirniDio, text='')
        height_spacer.grid(row=r+2, rowspan=4, columnspan=3)

if __name__ == '__main__':
    PyProfil()