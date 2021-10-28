import tkinter as tk
from tkinter import filedialog

print('selecione um arquivo: ')

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()


print('diretório do arquivo: ', file_path)
