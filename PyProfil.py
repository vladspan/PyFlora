from tkinter import *
from biljke_baza import *
from PyBiljka import Biljka
import os

class PyProfil():
    def __init__(self, root):
        self.bazniDio = Toplevel(root)
        self.bazniDio.geometry('800x800')
        self.okvirniDio = Frame(self.bazniDio)
        self.okvirniDio.pack(pady=50)
        
        plantData = BazaBilja().pretrazivanjeBiljke()
        
        self.images = []  # List to keep references to PhotoImage objects
        
        rowP = 0

        for biljka in plantData:
            self.scr(rowP, biljka)
            rowP += 2  # Each plant takes two rows

        self.addButton = Button(self.bazniDio, text='+', command=self.dodavanjeBiljke)
        self.addButton.pack(ipadx=20, ipady=20)
            
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
        spacer_label.grid(row=r, column=1, rowspan=2)
        
        # Verify if the image path is correct
        image_path = p[2]
        if not os.path.isfile(image_path):
            print(f"Image file does not exist: {image_path}")
            placeholder_image = PhotoImage(width=100, height=100)
            self.images.append(placeholder_image)  # Keep a reference to the placeholder image
            image_label = Label(self.okvirniDio, image=placeholder_image)
        else:
            plant_image = PhotoImage(file=image_path)
            self.images.append(plant_image)  # Keep a reference to the image
            image_label = Label(self.okvirniDio, image=plant_image)
        
        image_label.grid(row=r, column=2, rowspan=2, sticky="nsew")

        height_spacer = Label(self.okvirniDio, text='')
        height_spacer.grid(row=r+2, column=0, columnspan=3)

if __name__ == '__main__':
    root = Tk()
    PyProfil(root)
    root.mainloop()
