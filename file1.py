import tkinter as tk
from tkinter import filedialog
import cv2

print('selecione um arquivo: ')

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

print('diretório do arquivo: ', file_path)

file1 = cv2.subtract(cv2.imread("imagem1.jpg"), cv2.imread(file_path))

if file1.any():
    print("são diferentes")
else:
    print("são iguais.")
