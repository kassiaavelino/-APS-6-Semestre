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
          opc_menu_Func = int(input("Em que podemos ajudar? \n\n1.Mostrar dados\n2.Sair\n\nOpção: "))
          if(opc_menu_Func == 1):
               print("Dados obtidos:\n") 
               LerFuncionario()                            
               
               sys.exit()         

          elif(opc_menu_Func == 2):
               
               
               sys.exit()
          
          elif(opc_menu_Func >= 3):
               print("Opção inválida. Tente novamente!")
               

def menu_Diretor():
     while(True):
          opc_menu_Dire = int(input("Em que podemos ajudar? \n\n1.Mostrar dados\n2.Sair\n\nOpção: "))
          if(opc_menu_Dire == 1):
               print("Dados obtidos:\n") 
               LerDiretor()                            
               
               sys.exit()         
          elif(opc_menu_Dire == 2):
                              
               sys.exit()
          elif(opc_menu_Dire >= 3):
               print("Opção inválida. Tente novamente!")

def menu_Ministro():
     while(True):
          opc_menu_Mini = int(input("Em que podemos ajudar? \n\n1.Mostrar dados\n2.Sair\n\nOpção: "))
          if(opc_menu_Mini == 1):
               print("Dados obtidos:\n") 
               LerMinistro()                            
               
               sys.exit()         
          elif(opc_menu_Mini == 2):
                              
               sys.exit()
          elif(opc_menu_Mini >= 3):
               print("Opção inválida. Tente novamente!")
 
# nivel 1 - todos tem acesso
def funcionario():
     sleep(1)
     print("Seja Bem Vindo Funcionário!\n")
     sleep(1)  
     menu_Func()
     
     
# nivel 2 - somente diretores de divisão 
def diretor_div():
     sleep(1)
     print("Seja Bem Vindo Diretor!\n")
     sleep(1) 
     menu_Diretor()


# nivel 3 - somente ministro do meio ambiente
def ministro():
     sleep(1)
     print("Seja Bem Vindo Senhor Ministro!\n")
     sleep(1) 
     menu_Ministro()

def auth_func():     
     print('Lendo biometria.. \n')
     sleep(1)  

     file_path = filedialog.askopenfilename()

     file_path = os.path.basename(file_path)
     percentage = False

     try: 
          percentage = imgcompare.is_equal("bio1.jpg", file_path)
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
     img_aps = False

     try:
          img_aps = imgcompare.is_equal("bio2.jpg", file_path)
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
     img_aps1 = False

     try:
          img_aps1 = imgcompare.is_equal("bio3.jpg", file_path)
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