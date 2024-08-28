from tkinter import *
from biljke_baza import BazaBilja
from PyBiljka import Biljka

class PyProfil:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.baza = BazaBilja(username)
        self.root.title('PyFlora - Profil')

        self.frame = Frame(self.root)
        self.frame.pack(pady=20)

        self.label = Label(self.frame, text=f'Welcome, {username}', font=('Helvetica', 20))
        self.label.pack(pady=10)

        self.plantsFrame = Frame(self.frame)
        self.plantsFrame.pack(pady=20)

        self.addButton = Button(self.frame, text='+', command=self.addPlant)
        self.addButton.pack(pady=10)

        self.displayPlants()

    def displayPlants(self):
        for widget in self.plantsFrame.winfo_children():
            widget.destroy()

        plants = self.baza.pretrazivanjeBiljke()
        for plant in plants:
            plantFrame = Frame(self.plantsFrame)
            plantFrame.pack(fill='x', pady=5)

            textFrame = Frame(plantFrame)
            textFrame.pack(side=LEFT, fill='both', expand=True)

            nameLabel = Label(textFrame, text=plant[0], font=('Helvetica', 16, 'bold'))
            nameLabel.pack(anchor='w')

            descLabel = Label(textFrame, text=plant[1], font=('Helvetica', 12))
            descLabel.pack(anchor='w')

            try:
                img = PhotoImage(file=plant[2])
                imageLabel = Label(plantFrame, image=img)
                imageLabel.image = img  # Keep a reference to avoid garbage collection
                imageLabel.pack(side=RIGHT, padx=10)
            except Exception as e:
                print(f"Error loading image {plant[2]}: {e}")

    def addPlant(self):
        biljka = Biljka(self.username)
        biljka.biljkaProzor(self.root)
        self.displayPlants()

    def editPlant(self):

        pass
