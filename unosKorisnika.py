from tkinter import *
from korisnici_baza import *
from PyProfil import*

class UnosKorisnika:
    def __init__(self):
        self.baza = Baza()
        self.baza.createTable()
        self.refreshUserBaza()
        self.tkinterBaza = Tk()
        self.tkinterBaza.geometry('600x400')
        self.tkinterBaza.title('PyFlora')

        self.name = StringVar()
        self.sifra = StringVar()

        self.okvir = Frame(self.tkinterBaza)
        self.okvir.pack(pady=50)

        self.naslov = Label(self.okvir, text='PyFlora', foreground='orange', font=('Helvetica', 24, 'normal', 'roman'))
        self.naslov.grid(row=0, columnspan=2)

        self.spacer = Label(self.okvir, text='')
        self.spacer.grid(row=1, columnspan=2, pady=20)

        self.naslovUsername = Label(self.okvir, text='Username', foreground='grey', font=('Helvetica', 16, 'normal', 'roman'))
        self.naslovUsername.grid(row=2, column=0)

        self.unosUsername = Entry(self.okvir, textvariable=self.name)
        self.unosUsername.grid(row=3, column=0)

        self.naslovPassword = Label(self.okvir, text='Password', foreground='grey', font=('Helvetica', 16, 'normal', 'roman'))
        self.naslovPassword.grid(row=2, column=1)

        self.unosPassword = Entry(self.okvir, textvariable=self.sifra, show='*')
        self.unosPassword.grid(row=3, column=1)

        self.buttonUser = Button(self.okvir, text='Sign up', command=self.userSignUp)
        self.buttonUser.grid(row=4, column=0)

        self.buttonUserLogin = Button(self.okvir, text='Sign in', command=self.userSignIn)
        self.buttonUserLogin.grid(row=4, column=1)

        self.errorMessage = Label(self.okvir, text='', foreground='red', font=('Helvetica', 12, 'normal', 'roman'))
        self.errorMessage.grid(row=5, columnspan=2, pady=10)

        self.okvir.mainloop()

    def refreshUserBaza(self):
        self.userBaza = self.baza.pretrazivanjeKorisnika()
        print(f'refreshUserBaza: {self.userBaza}')  # Debug print

    def userSignUp(self):
        self.refreshUserBaza()
        userName = self.name.get()
        sifra = self.sifra.get()

        if not userName or not sifra:
            self.errorMessage.config(text='Error: Username and Password cannot be empty')
            self.errorMessage.after(3000, lambda: self.errorMessage.config(text=''))
        else:
            self.errorMessage.config(text='')
            print(f'Username: {userName}, Password: {sifra}')
            
            if any(len(user) > 0 and user[0] == userName for user in self.userBaza):
                self.errorMessage.config(text="Username exists. Please try another username.")
                self.errorMessage.after(3000, lambda: self.errorMessage.config(text=''))
                self.tkinterBaza.after(3000, self.clearEntries)
            else: 
                self.baza.dodavanjeKorisnika(userName, sifra)
                self.refreshUserBaza()
                self.errorMessage.config(text=f'Sign up successful!\nWelcome {userName.upper()}', foreground='green')
                self.errorMessage.after(3000, lambda: self.errorMessage.config(text='', foreground='red'))
                self.tkinterBaza.after(3000, self.clearEntries)

    def userSignIn(self):
        self.refreshUserBaza()
        userName = self.name.get()
        sifra = self.sifra.get()

        print(f'userSignIn: {self.userBaza}')  # Debug print

        if any(len(user) > 1 and user[0] == userName and user[1] == sifra for user in self.userBaza):
            print(f'Login successful for user: {userName}')  # Debug print
            PyProfil()
          
        else:
            self.errorMessage.config(text='Invalid username or password')
            self.errorMessage.after(3000, lambda: self.errorMessage.config(text=''))
            print(f'Login failed for user: {userName}')  # Debug print
            
    def clearEntries(self):
        self.name.set('')
        self.sifra.set('')

if __name__ == '__main__':
    UnosKorisnika()
