from tkinter import *
from tkinter import messagebox
from biljke_baza import BazaBilja
from PyProfil import PyProfil

class UnosKorisnika:
    def __init__(self, root):
        self.root = root
        self.root.title('PyFlora - Unos korisnika')

        self.frame = Frame(self.root)
        self.frame.pack(pady=20)

        self.labelUser = Label(self.frame, text='Korisničko ime:')
        self.labelUser.grid(row=0, column=0, pady=5)
        self.entryUser = Entry(self.frame)
        self.entryUser.grid(row=0, column=1, pady=5)

        self.labelPass = Label(self.frame, text='Lozinka:')
        self.labelPass.grid(row=1, column=0, pady=5)
        self.entryPass = Entry(self.frame, show='*')
        self.entryPass.grid(row=1, column=1, pady=5)

        self.loginButton = Button(self.frame, text='Login', command=self.userSignIn)
        self.loginButton.grid(row=2, column=0, columnspan=2, pady=10)

        self.signupButton = Button(self.frame, text='Sign Up', command=self.userSignUp)
        self.signupButton.grid(row=3, column=0, columnspan=2, pady=10)

    def userSignIn(self):
        username = self.entryUser.get()
        password = self.entryPass.get()

        if not username or not password:
            messagebox.showerror('Error', 'All fields are required')
            return

        baza = BazaBilja(username)
        user = baza.provjeraKorisnika(username, password)
        if user:
            self.root.destroy()
            root = Tk()
            app = PyProfil(root, username)
            root.mainloop()
        else:
            messagebox.showerror('Error', 'Invalid credentials')

    def userSignUp(self):
        username = self.entryUser.get()
        password = self.entryPass.get()

        if not username or not password:
            messagebox.showerror('Error', 'All fields are required')
            return

        baza = BazaBilja(username)
        baza.dodavanjeKorisnika(username, password)
        messagebox.showinfo('Success', f'User {username} signed up successfully')
