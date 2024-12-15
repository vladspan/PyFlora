from tkinter import *
from biljke_baza import BazaBilja
from PyBiljka import Biljka

class PyProfil:
    def __init__(self, root, username):

        self.root = root 
        self.root.title('PyFlora - Profil')
        self.username = username

        #Initialiaze the database coonection
        self.baza = BazaBilja(self.username)

        #Create GUI components
        self.cretaeWidgets()

        #Display the plants in the user's profile
        self.displayPlants()


    def cretaeWidgets(self):
        
        #Frame for plan entries
        self.plantsFrame = Frame(self.root)
        self.plantsFrame.pack(pady=20)

        #Button to add a new plant
        self.addPlantButton = Button(self.root, text='+', command= self.addPlant)
        self.addPlantButton.pack(pady=10)

        #Button to edit the selecetd plant
        self.editPlantButton = Button(self.root, text='Edit', command=self.editPlant)
        self.editPlantButton.pack(pady=10)

        #Listbox to display plants
        self.plantListBox = Listbox(self.plantsFrame)
        self.plantListBox.pack(side=LEFT, fill=BOTH, expand=True )

        #Scrollbar for the listbox
        self.scrollbar = Scrollbar(self.plantsFrame, orient=VERTICAL)
        self.scrollbar.config(command=self.plantListBox.yview)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.plantListBox.config(yscrollcommand=self.scrollbar.set)


    def displayPlants(self):
        
        self.plantListBox.delete(0,END)

        plants = self.baza.pretrazivanjeBiljke()
        for plant in plants:
            displayText = f'{plant[0]}: {plant[1]}'
            self.plantListBox.insert(END, displayText)
            

    def addPlant(self):
        #Open a window to add a plant
        self.newPlantWindow = Toplevel(self.root)
        Biljka().biljkaProzor(self.newPlantWindow)

    def editPlant(self):
        #Get the selected plant
        selectedIndex = self.plantListBox.curselection()
        if not selectedIndex:
            self.messagebox.showerror("Error", "Please select a plant to edit.")
            return
        
        selectedText = self.plantListBox.get(selectedIndex)
        plantName = selectedText.split(':')[0]

        #Retrive the plant details from the database
        plantData = self.baza.dohvatiBiljkuImenom(plantName.strip())

        if plantData:
            #Opent the plant edit window with pre-filled data
            self.editPlantWindow = Toplevel(self.root)
            Biljka().biljkaProzor(self.editPlantWindow, plantData)

    def refreshPlants(self):
        self.displayPlants()


