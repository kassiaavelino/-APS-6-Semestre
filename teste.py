import tkinter as tk
from tkinter import filedialog
import imgcompare
import os
import sys
from time import sleep
from conectmysql import *

root = tk.Tk() 
root.withdraw()

def menu_Func():
     while(True):
          opc_menu_Func = int(input("1"))
          if(opc_menu_Func == 1):
               print("")               
               auth_func()          
          elif(opc_menu_Func == 2):
               print("")
               auth_diretor()
          elif(opc_menu_Func == 3):
               print("")
               auth_ministro()
          elif(opc_menu_Func >= 4):
               sys.exit()

def menu_Diretor():
     while(True):
          opc_menu_Func = int(input(""))
          if(opc_menu_Func == 1):
               print("")               
               auth_func()          
          elif(opc_menu_Func == 2):
               print("")
               auth_diretor()
          elif(opc_menu_Func == 3):
               print("")
               auth_ministro()
          elif(opc_menu_Func >= 4):
               sys.exit()

def menu_Ministro():
     while(True):
          opc_menu_Func = int(input(""))
          if(opc_menu_Func == 1):
               print("")               
               auth_func()          
          elif(opc_menu_Func == 2):
               print("")
               auth_diretor()
          elif(opc_menu_Func == 3):
               print("")
               auth_ministro()
          elif(opc_menu_Func >= 4):
               sys.exit()

# nivel 1 - todos tem acesso
def funcionario():
     sleep(1)
     print("Seja Bem Vindo Funcionário!\n")
     sleep(1)  
     LerFuncionario()
     
     sys.exit()
     
# nivel 2 - somente diretores de divisão 
def diretor_div():
     sleep(1)
     print("Seja Bem Vindo Diretor!\n")
     sleep(1) 
     LerDiretor()

     sys.exit()

# nivel 3 - somente ministro do meio ambiente
def ministro():
     sleep(1)
     print("Seja Bem Vindo Senhor Ministro!\n")
     sleep(1) 
     LerMinistro()

     sys.exit()

def auth_func():     
     print('Lendo biometria.. \n')
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
          
          funcionario() 
 
     else:     
          print("Falha na leitura biométrica\n")
          sys.exit()

def auth_diretor():
     print('Lendo biometria.. \n')
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
          
          diretor_div()
     else:     
          print("Falha na leitura biométrica\n")
          sys.exit()

def auth_ministro():
     print('Lendo biometria.. \n')
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

          ministro()
     
     else:     
          print("Falha na leitura biométrica\n")
          sys.exit()

# menu para seleção do usuario desejado
def menu():
     while(True):
          opcMenu = int(input("Selecione o usuário: \n\n1.Funcionário\n2.Diretor\n3.Ministro\n4.Sair\n\nOpção: "))
          if(opcMenu == 1):
               print("Por favor faça a leitura biométrica Funcionário X\n")               
               auth_func()          
          elif(opcMenu == 2):
               print("Por favor faça a leitura biométrica Diretor")
               auth_diretor()
          elif(opcMenu == 3):
               print("Por favor faça a leitura biométrica Ministro")
               auth_ministro()
          elif(opcMenu >= 4):
               sys.exit()

print("Bem vindo!\n")
sleep(1)
menu()