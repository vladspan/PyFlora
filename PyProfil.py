from tkinter import *
from tkinter import messagebox
from biljke_baza import BazaBilja
from PyBiljka import Biljka

class PyProfil:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.baza = BazaBilja(self.username)

        self.root.title(f'PyProfil - {self.username}')

        # Add a Logout button in the upper-right corner
        logout_button = Button(self.root, text='Logout', command=self.logout, fg='red')
        logout_button.pack(anchor='ne', padx=10, pady=10)

        self.listbox = Listbox(self.root, width=50)
        self.listbox.pack(pady=20)

        Button(self.root, text='+', command=self.addPlant).pack(pady=5)
        Button(self.root, text='Edit', command=self.editPlant).pack(pady=5)

        self.refreshList()

    def refreshList(self):
        """Refresh the Listbox with plant names."""
        self.listbox.delete(0, END)
        plants = self.baza.pretrazivanjeBiljke()
        for plant in plants:
            self.listbox.insert(END, plant[2])  # Plant name (column 2)

    def addPlant(self):
        """Open a window to add a new plant."""
        biljka = Biljka(self.username)
        biljka.biljkaProzor(self.root, refresh_callback=self.refreshList)

    def editPlant(self):
        """Open a window to edit the selected plant."""
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showerror('Error', 'Please select a plant to edit')
            return
        
        selected_name = self.listbox.get(selected_index)
        plants = self.baza.pretrazivanjeBiljke()
        for plant in plants:
            if plant[2] == selected_name:  # Match plant name
                biljka = Biljka(self.username)
                biljka.biljkaProzor(self.root, plantData=plant, refresh_callback=self.refreshList)
                break

    def logout(self):
        """Handle the logout action."""
        self.root.destroy()
        from unosKorisnika import UnosKorisnika  # Avoid circular import
        main_root = Tk()
        UnosKorisnika(main_root)
        main_root.mainloop()
        
    



