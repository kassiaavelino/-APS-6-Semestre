from tkinter import * 

root = Tk()

canvas = Canvas(width=400,height=250, bg='blue')
canvas.pack()
photo = PhotoImage(file='imagem4.png')

canvas.create_image(0,0, image=photo, anchor=NW)

root.mainloop()