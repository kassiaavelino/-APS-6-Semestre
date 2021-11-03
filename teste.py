import tkinter as tk
from tkinter import filedialog
import imgcompare
import os
import sys
from time import sleep

root = tk.Tk() 
root.withdraw()
# nivel 1 - todos tem acesso
def funcionarioX():
     sleep(1)
     print("Seja Bem Vindo FuncionárioX!")
     sys.exit()
     
# nivel 2 - somente diretores de divisão 
def diretor_div():
     sleep(1)
     print("Seja Bem Vindo Diretor!")

# nivel 3 - somente ministro do meio ambiente
def ministro():
     sleep(1)
     print("Seja Bem Vindo Senhor Ministro!")

def compare1():     
     print('Lendo biometria.. ')
     sleep(1)  

     file_path = filedialog.askopenfilename()

     file_path = os.path.basename(file_path)
     percentage = False 
     img_aps = False
     img_aps1 = False


     try: 
          percentage = imgcompare.is_equal("imagem1.jpg", file_path)
     except:
          print("Erro na leitura biométrica,\n Tente Novamente!")
          menu()

     if  percentage:
          # print("são iguais.")
          # print("imagem selecionada: ", file_path)
          funcionarioX() 

     # elif img_aps1:
     #      # print ("são iguais")
     #      print("imagem selecionada: ", file_path)
     #      ministro()

     else:     
          print("Falha na leitura biométrica\n")
          sys.exit()
def compare2():
     print('Lendo biometria.. ')
     sleep(1)   

     file_path = filedialog.askopenfilename()

     file_path = os.path.basename(file_path)
     percentage = False 
     img_aps = False
     img_aps1 = False

     try:
          img_aps = imgcompare.is_equal("imagem2.jpg", file_path)
     except:
          pass
     
     if img_aps:
          # print ("são iguais")
          # print("imagem selecionada: ", file_path)
          diretor_div()
     else:     
          print("Falha na leitura biométrica\n")
          sys.exit()


def compare3():
     print('Lendo biometria.. ')
     sleep(1)  

     file_path = filedialog.askopenfilename()

     file_path = os.path.basename(file_path)
     percentage = False 
     img_aps = False
     img_aps1 = False

     try:
          img_aps1 = imgcompare.is_equal("imagem3.jpg", file_path)
     except:
          pass

     if img_aps1:
          # print ("são iguais")
          # print("imagem selecionada: ", file_path)
          ministro()
     
     else:     
          print("Falha na leitura biométrica\n")
          sys.exit()

def menu():
     while(True):
          opcMenu = int(input("Selecione o usuário: \n\n1.Funcionário\n2.Diretor\n3.Ministro\n4.Sair\n\nOpção: "))
          if(opcMenu == 1):
               print("Por favor faça a leitura biométrica Funcionário X\n")               
               compare1()          
          elif(opcMenu == 2):
               print("Por favor faça a leitura biométrica Diretor")
               compare2()
          elif(opcMenu == 3):
               print("Por favor faça a leitura biométrica Ministro")
               compare3()
          elif(opcMenu >= 4):
               sys.exit()

print("Bem vindo!\n")
sleep(1)
menu()