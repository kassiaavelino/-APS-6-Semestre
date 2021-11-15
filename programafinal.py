import tkinter as tk
from tkinter import filedialog
import imgcompare
import os
import sys
from time import sleep
from conectmysql import *
from tkinter import *

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
          

     if  percentage:
          
          janela_func() 
 
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
          
          janela_diretor()
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
            
          janela_ministro()
     
     else:     
          print("Falha na leitura biométrica\n")
          sys.exit()

def janela_func():
    jn_func = tk.Toplevel(janela)
    labelfunc = Label (jn_func, text='Seja Bem Vindo Funcionário!')
    labelfunc.grid(column=0, row=0)
    
    btn_func_dados = Button(jn_func, text="Mostrar dados", command=LerFuncionario)
    btn_func_dados.grid(column=0, row=1)
    btn_func_sair = Button(jn_func, text="Sair", command=quit)
    btn_func_sair.grid(column=1, row=3)
   

def janela_diretor():
    jn_di = tk.Toplevel(janela)
    labelfunc = Label (jn_di, text='Seja Bem Vindo Diretor!')
    labelfunc.grid(column=0, row=0)
    
    btn_func_dados = Button(jn_di, text="Mostrar dados", command=LerDiretor)
    btn_func_dados.grid(column=0, row=1)
    btn_func_sair = Button(jn_di, text="Sair", command=quit)
    btn_func_sair.grid(column=1, row=3)

def janela_ministro():
    jn_min = tk.Toplevel(janela)
    labelfunc = Label (jn_min, text='Seja Bem Vindo Ministro!')
    labelfunc.grid(column=0, row=0)
    
    btn_func_dados = Button(jn_min, text="Mostrar dados", command=LerMinistro)
    btn_func_dados.grid(column=0, row=1)
    btn_func_sair = Button(jn_min, text="Sair", command=quit)
    btn_func_sair.grid(column=1, row=3)   
    
janela=Tk()
janela.title("Programa de reconhecimento biometrico")
janela.geometry('460x150')
infoJanela = Label (janela, text = "Bem vindo ao Programa de Biometria", font='broadway')
infoJanela.grid(column=1, row=0)

infoJanela1 = Label (janela, text = "Por favor, escolha a sua opção de Login", font='georgia')
infoJanela1.grid(column=1, row=1)

botao1 = Button(janela, text="Funcionario", command=auth_func)
botao1.grid(column=0, row=2)

botao2 = Button(janela, text="Diretor", command=auth_diretor)
botao2.grid(column=1, row=2)

botao3 = Button(janela, text="Ministro", command=auth_ministro)
botao3.grid(column=2, row=2)

lbl_space = Label (janela, text = "")
lbl_space.grid(column=1, row=3)

botao4 = Button(janela, text="Sair", command=quit)
botao4.grid(column=2, row=4)

janela.mainloop()

janela1=Tk()
janela1.title("biometria")
infoJanela1 = Label (janela1, text = "Bem vindo ao Programa de Biometria")
infoJanela1.grid(column=1, row=0)
janela.mainloop()



# menu para seleção do usuario desejado
# def menu():
#      while(True):
#           opcMenu = int(input("Selecione o usuário: \n\n1.Funcionário\n2.Diretor\n3.Ministro\n4.Sair\n\nOpção: "))
#           if(opcMenu == botao1):
#                print("Por favor faça a leitura biométrica Funcionário X\n")               
#                auth_func()          
#           elif(opcMenu == 2):
#                print("Por favor faça a leitura biométrica Diretor")
#                auth_diretor()
#           elif(opcMenu == 3):
#                print("Por favor faça a leitura biométrica Ministro")
#                auth_ministro()
#           elif(opcMenu >= 4):
#                sys.exit()

# print("Bem vindo!\n")
# sleep(1)
# menu()