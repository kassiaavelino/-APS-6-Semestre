import tkinter as tk
from tkinter import filedialog
import imgcompare
import os

print('selecione um arquivo: ')

root = tk.Tk() 
root.withdraw()

file_path = filedialog.askopenfilename()

file_path = os.path.basename(file_path)

percentage = False 
try:
   percentage = imgcompare.is_equal("imagem1.jpg", file_path)
except:
    pass

if  percentage:
     print("são iguais.") 
else:
     print("são diferentes")