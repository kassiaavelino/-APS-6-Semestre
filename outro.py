#!/usr/bin/env python
# -*- coding: latin-1 -*-
# Desenvolvimento Aberto
# visual.py
 
# importa modulo
from tkinter import *
 
# Cria formulario
formulario = Tk()
formulario.title = "Desenvolvimento Aberto"
 
# Alimenta variaveis do label
r = StringVar()
r= "Resultado"
 
# Evento do botão
def callback():
    r = texto1.get() + texto2.get()
    resultado = Label(formulario, text = r)
    resultado.grid(row=4, column=1)
 
# Cria um novo label
rotulo = Label(formulario, text = "Concatena Strings")
texto1 = Entry(formulario)
texto2 = Entry(formulario)
botao =  Button(formulario, text = "Somar", command = callback)
resultado = Label(formulario, text = r)
 
# Adiciona Componentes no Grid
rotulo.grid(row=0, column=1)
texto1.grid(row=1, column=1)
texto2.grid(row=2, column=1)
botao.grid(row=3, column=1)
resultado.grid(row=4, column=1)
 
# Roda o loop principal do tcl
mainloop()