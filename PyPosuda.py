from tkinter import*
from unosKorisnika import*


class Posuda:
    def __init__(self):
        
        self.bazniOkvir = Tk()
        self.bazniOkvir.geometry('600x800')
        self.bazniOkvir.title('PyPosuda')

        self.okvir = Frame(self.bazniOkvir)
        self.okvir.pack(pady=50)

        self.oznakaIme = Label(self.okvir, text='Ime',foreground='orange', font=('Helvetica', 24, 'normal', 'roman'))
        self.oznakaIme.pack(padx=20)

        self.bazniOkvir.mainloop()

