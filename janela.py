import tkinter as tk
from tkinter import *
jn_func = tk.Tk()
jn_func.geometry('700x300')
labelfunc = Label (jn_func, text='Seja Bem Vindo Funcionário!')
labelfunc.grid(column=0, row=0)
    
#     btn_func_dados = Button(jn_func, text="Mostrar dados", command=LerFuncionario)
#     btn_func_dados.grid(column=0, row=1)
btn_func_sair = Button(jn_func, text="Sair", command=quit)
btn_func_sair.grid(column=1, row=3)
    
canvas = tk.Canvas(jn_func)
canvas.grid(column=0, row=2)
canvas_t = canvas.create_text(10,10, text="",anchor=tk.NW)
our_text = '''
        ┌─────────────────────────────────────────────────┐
        │   NOME                  │  TELEFONE  │  NIVEL DE CONTAMINAÇÃO   │
        └─────────────────────────────────────────────────┘
          Marcos Antonio da Silva       (43)85587-6144  Alto
          Daniella Costa Nunes          (15)65365-0944  Médio
          Fernanda Souza                (83)31058-9438  Baixo
          Felipe Lima Andrade           (38)71157-8329  Baixo
          Sophia dos Santos Duarte      (68)76925-8613  Alto
          Raphael da Costa              (60)30472-1325  Alto
          Gabriel Fernandes Lima        (25)40542-4676  Baixo
                         '''
new_text = canvas.itemconfigure(canvas_t, text=our_text)
canvas.after(new_text)
jn_func.mainloop()