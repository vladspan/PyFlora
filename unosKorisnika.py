from tkinter import *
from tkinter import messagebox
from biljke_baza import BazaBilja
from PyProfil import PyProfil

class UnosKorisnika:
    def __init__(self, root):
        self.root = root
        self.root.title('PyFlora - Login')

        frame = Frame(self.root)
        frame.pack(pady=20)

        Label(frame, text='Username:').grid(row=0, column=0, pady=5)
        self.username = Entry(frame)
        self.username.grid(row=0, column=1, pady=5)

        Label(frame, text='Password:').grid(row=1, column=0, pady=5)
        self.password = Entry(frame, show='*')
        self.password.grid(row=1, column=1, pady=5)

        Button(frame, text='Login', command=self.login).grid(row=2, column=0, columnspan=2, pady=10)
        Button(frame, text='Sign Up', command=self.signup).grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username.get()
        password = self.password.get()
        baza = BazaBilja(username)

        if baza.provjeraKorisnika(username, password):
            self.root.destroy()
            root = Tk()
            PyProfil(root, username)
            root.mainloop()
        else:
            messagebox.showerror('Error', 'Invalid credentials')

    def signup(self):
        username = self.username.get()
        password = self.password.get()
        baza = BazaBilja(username)
        baza.dodavanjeKorisnika(username, password)
        messagebox.showinfo('Success', 'User signed up successfully')