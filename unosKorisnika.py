from tkinter import*


class UnosKorisnika:
    def __init__(self) -> None:
        self.tkinterBaza = Tk()
        self.tkinterBaza.geometry('600x400')
        self.tkinterBaza.title('PyFlora')
        
        self.okvir = Frame(self.tkinterBaza)
        self.okvir.pack(pady=50)

        self.naslov = Label(self.okvir, text='Sign up', foreground='orange', font=('Helvetica', 24, 'normal', 'roman'))
        self.naslov.grid(row=0, columnspan=2)

        self.spacer = Frame(self.okvir)
        self.spacer.grid(pady=50)

        self.naslovUsername = Label(self.okvir, text='Username', foreground='grey', font=('Helvetica', 16, 'normal', 'roman'))
        self.naslovUsername.grid(row=2, column=0)

        self.unosUsername = Entry(self.okvir)
        self.unosUsername.grid(row=3, column=0)

        self.naslovUsername = Label(self.okvir, text='Password', foreground='grey', font=('Helvetica', 16, 'normal', 'roman'))
        self.naslovUsername.grid(row=2, column=1)

        self.unosUsername = Entry(self.okvir)
        self.unosUsername.grid(row=3, column=1)

        self.okvir.mainloop()


if __name__ == '__main__':
    UnosKorisnika()