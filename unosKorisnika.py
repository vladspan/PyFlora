from tkinter import*
from korisnici_baza import*


class UnosKorisnika:
    def __init__(self) -> None:
        
        self.tkinterBaza = Tk()
        self.tkinterBaza.geometry('600x400')
        self.tkinterBaza.title('PyFlora')

        self.name = StringVar()
        self.sifra = StringVar()
        
        self.okvir = Frame(self.tkinterBaza)
        self.okvir.pack(pady=50)

        self.naslov = Label(self.okvir, text='Sign up', foreground='orange', font=('Helvetica', 24, 'normal', 'roman'))
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

        self.buttonUser = Button(self.okvir, text='Sign up', command=self.userLogin)
        self.buttonUser.grid(row=4, columnspan=2)

        self.errorMessage = Label(self.okvir, text='', foreground='red', font=('Hevletica', 12, 'normal', 'roman'))
        self.errorMessage.grid(row=5, columnspan=2, pady=10)

        self.okvir.mainloop()
        
    def userLogin(self):
        userName = self.name.get()
        sifra = self.sifra.get()

        if not userName or not sifra:
            self.errorMessage.config(text='Error: Username and Password cannot be empty')
            self.errorMessage.after(3000, lambda: self.errorMessage.config(text=''))

        else:
            self.errorMessage.config(text='')
            print(f'Username: {userName}, Password: {sifra}')
        
        Baza().noviKorisnik(userName,sifra) 
        

if __name__ == '__main__':
    UnosKorisnika()
