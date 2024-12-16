from tkinter import *
from unosKorisnika import*


def center_window(window, width=450, height=350):
    """Center a Tkinter window on the screen."""
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_offset = (screen_width - width) // 2
    y_offset = (screen_height - height) // 2
    window.geometry(f'{width}x{height}+{x_offset}+{y_offset}')


if __name__ == '__main__':
    root = Tk()  # Only one main Tk() instance
    center_window(root)
    UnosKorisnika(root)
    root.mainloop()


