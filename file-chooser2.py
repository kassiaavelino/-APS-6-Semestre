from tkinter import *

root = Tk()

class Img_load:
    def __init__(self):
        self.root = root
        self.img = PhotoImage(file= "foto.png")
        a1 = Label(root,image=self.img)
        a1.place(x=0,y=0,relwidth=1,relheight=1)
        root.mainloop()
Img_load()