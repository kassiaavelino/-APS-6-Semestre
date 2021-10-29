import tkinter as tk
from tkinter import filedialog
import imgcompare
import os


# nivel 1 - todos tem acesso
def funcionarioX():
     print("Seja Bem Vindo!")
     
# nivel 2 - somente diretores de divisão 
def diretor_div():
     print("Seja Bem Vindo Diretor!")

# nivel 3 - somente ministro do meio ambiente
def ministro():
     print("Seja Bem Vindo Senhor Ministro!")

def menu():
     while(True):
          opcMenu = int(input("Selecione o usuário: \n\n1.Funcionário\n2.Diretor\n3.Ministro\n4.Sair\n\nOpção: "))
          if(opcMenu == 1):
               print("usuário 1")
               break
          elif(opcMenu == 2):
               print("usuário 2")
               break
          elif(opcMenu == 2):
               print("usuário 3")
               break

print("Bem vindo!")
menu()     
print('Selecione um arquivo: ')
def open_file():
     root = tk.Tk() 
     root.withdraw()

file_path = filedialog.askopenfilename()

file_path = os.path.basename(file_path)
open_file()
percentage = False 
img_aps = False
img_aps1 = False


try: 
    percentage = imgcompare.is_equal("imagem1.jpg", file_path)
except:
    pass
try:
     img_aps = imgcompare.is_equal("imagem2.jpg", file_path)
except:
     pass
try:
     img_aps1 = imgcompare.is_equal("imagem3.jpg", file_path)
except:
     pass

if  percentage:
     # print("são iguais.")
     print("imagem selecionada: ", file_path)
     funcionarioX() 

elif img_aps:
     # print ("são iguais")
     print("imagem selecionada: ", file_path)
     diretor_div()

elif img_aps1:
     # print ("são iguais")
     print("imagem selecionada: ", file_path)
     ministro()

else:     
     print("Falha na leitura biométrica\n")
     menu()