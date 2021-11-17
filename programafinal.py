import tkinter as tk
from tkinter import filedialog
from tkinter.font import BOLD
import imgcompare
import os
import sys
from conectmysql import *
from tkinter import *

root = tk.Tk() 
root.withdraw()

def auth_func():     
     print('Lendo biometria.. \n') 

     file_path = filedialog.askopenfilename()
     file_path = os.path.basename(file_path)
     bio_funcionario = False

     try: 
          bio_funcionario = imgcompare.is_equal("bio1.jpg", file_path)
     except:
          print("Erro na leitura biométrica,\n Tente Novamente!")          

     if  bio_funcionario:          
          janela_func()
     else:     
          print("Falha na leitura biométrica\n")
          sys.exit()

def auth_diretor():
     print('Lendo biometria.. \n')  

     file_path = filedialog.askopenfilename()
     file_path = os.path.basename(file_path)
     bio_diretor = False

     try:
          bio_diretor = imgcompare.is_equal("bio2.jpg", file_path)
     except:
          pass
     
     if bio_diretor:          
          janela_diretor()
     else:     
          print("Falha na leitura biométrica\n")
          sys.exit()

def auth_ministro():
     print('Lendo biometria.. \n') 

     file_path = filedialog.askopenfilename()
     file_path = os.path.basename(file_path)
     bio_ministro = False

     try:
          bio_ministro = imgcompare.is_equal("bio3.jpg", file_path)
     except:
          pass

     if bio_ministro:            
          janela_ministro()     
     else:     
          print("Falha na leitura biométrica\n")
          sys.exit()

def janela_func():
     jn_func = tk.Toplevel(janela)
     jn_func.geometry('550x300')
     jn_func.configure(bg='#B3EFB5')
     labelfunc = Label (jn_func, text='Seja Bem Vindo Funcionário!',font=('georgia',15,'bold'),fg='#182B19',bg='#B3EFB5')
     labelfunc.place(x=130, y=5)
     labelfunc1 = Label (jn_func, text='Dados coletados até o momento',font=('georgia',11),fg='#182B19',bg='#B3EFB5')
     labelfunc1.place(x=175, y=30)
     
     btn_func_sair = Button(jn_func, text="Sair", command=quit)
     btn_func_sair.place(x=510, y=270)
    
     canvasfun = tk.Canvas(jn_func, width= 500, height=200,bg='#B3EFB5')
     canvasfun.place(x=20, y=60)
     canvas_x = canvasfun.create_text(10,10, text="",anchor=tk.NW)
     our_text = '''
        ┌───────────────────────────────────┐ 
        │                NOME               │       TELEFONE       │     NIVEL DE CONTAMINAÇÃO   │
        └───────────────────────────────────┘
          Marcos Antonio da Silva        (43)85587-6144           Alto
          Daniella Costa Nunes             (15)65365-0944           Médio
          Fernanda Souza                       (83)31058-9438           Baixo
          Felipe Lima Andrade               (38)71157-8329           Baixo
          Sophia dos Santos Duarte      (68)76925-8613           Alto
          Raphael da Costa                     (60)30472-1325          Alto
          Gabriel Fernandes Lima          (25)40542-4676           Baixo
                         '''
     canvasfun.itemconfigure(canvas_x, text=our_text)
       
def janela_diretor():
     jn_di = tk.Toplevel(janela)
     jn_di.configure(bg='#B3EFB5')
     jn_di.geometry('700x400')
     labeldir = Label (jn_di, text='Seja Bem Vindo Diretor!',font=('georgia',15,'bold'),fg='#182B19',bg='#B3EFB5')
     labeldir.place(x=220, y=5)
     labeldir1 = Label (jn_di, text='Dados coletados até o momento',font=('georgia',11),fg='#182B19',bg='#B3EFB5')
     labeldir1.place(x=235, y=50)
    
     btn_dir_sair = Button(jn_di, text="Sair", command=quit)
     btn_dir_sair.place(x=650, y=370)
    
     canvasdir = tk.Canvas(jn_di, width= 650, height=250,bg='#B3EFB5')
     canvasdir.place(x=20, y=80)
     canvas_y = canvasdir.create_text(10,10, text="",anchor=tk.NW)
     our_text = '''
     ┌─────────────────────────────────────────────────┐
     │                NOME                 │      TELEFONE      │  AREA  │  TIPO AGROTÓXICO  │  NIVEL DE CONTAMINAÇÃO  │
     └─────────────────────────────────────────────────┘
        Marcos Antonio da Silva        (43)85587-6144         5km²              Herbicidas                                     Alto 
        Daniella Costa Nunes             (15)65365-0944         30km²            Bactericidas                                   Médio 
        Fernanda Souza                       (83)31058-9438         2km²              Fungicidas                                     Baixo 
        Felipe Lima Andrade               (38)71157-8329         5km²              Herbicidas                                     Baixo 
        Sophia dos Santos Duarte      (68)76925-8613         30km²            Inseticidas                                      Alto 
        Raphael da Costa                     (60)30472-1325        12km²             Bactericidas                                   Alto 
        Gabriel Fernandes Lima          (25)40542-4676         7km²              Herbicidas                                     Baixo 
                         '''
     canvasdir.itemconfigure(canvas_y, text=our_text)

def janela_ministro():
     jn_min = tk.Toplevel(janela)
     jn_min.configure(bg='#B3EFB5')
     jn_min.geometry('1300x450')
     labelmini = Label (jn_min, text='Seja Bem Vindo Ministro!',font=('georgia',15,'bold'),fg='#182B19',bg='#B3EFB5')
     labelmini.place(x=485,y=15)
     labelmini1 = Label (jn_min, text='Dados coletados até o momento',font=('georgia',11),fg='#182B19',bg='#B3EFB5')
     labelmini1.place(x=510,y=60)
    
     btn_dir_sair = Button(jn_min, text="Sair", command=quit)
     btn_dir_sair.place(x=1250,y=420)
    
     canvasmini = tk.Canvas(jn_min, width= 1250, height=300,bg='#B3EFB5')
     canvasmini.pack()
     canvasmini.place(x=20, y=90)
     canvas_z = canvasmini.create_text(5,5, text="",anchor=tk.NW)
     
     our_text = '''
     ┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
     │                  NOME                    │           CPF           │      TELEFONE      │                                                               ENDEREÇO                                                                            │   AREA   │   TIPO AGROTÓXICO   │ NIVEL DE CONTAMINAÇÃO  │
     └────────────────────────────────────────────────────────────────────────────────────────────────────┘
      Marcos Antonio da Silva               005.406.740-52       (43)85587-6144         Avenida Ponta Negra, Praia do Amapá - Rio Branco (AC)                                                                 5km²            Herbicidas                          Alto
      Daniella Costa Nunes                    883.978.650-39       (15)65365-0944         Quadra 1106 Sul Alameda 51, Plano Diretor Sul - Palmas (TO)                                                          30km²          Bactericidas                       Médio
      Fernanda Souza                             212.145.510-84       (83)31058-9438         Rua Alto Paraguai, Mapim - Várzea Grande (MT)                                                                                 2km²            Fungicidas                         Baixo
      Felipe Lima Andrade                     588.114.650-60       (38)71157-8329         Rua Palmeira, Jacaré - Rio de Janeiro (RJ)                                                                                             5km²             Herbicidas                          Baixo
      Sophia dos Santos Duarte             791.395.880-41       (68)76925-8613         Rua Vera Cruz, Alecrim - Vila Velha (ES)                                                                                                30km²          Inseticidas                          Alto
      Raphael da Costa                           406.683.560-06       (60)30472-1325         Rua Antônia Leite Rangel, Parque Residencial Rochelle - Santa Bárbara D`Oeste (SP)                   12km²          Bactericidas                        Alto    
      Gabriel Fernandes Lima                 544.646.000-69       (25)40542-4676         Rua Pio XII, São José - Caxias do Sul (RS)                                                                                              7km²            Herbicidas                         Baixo
                         '''
     canvasmini.itemconfigure(canvas_z, text=our_text)
    
janela=Tk()
janela.title("Ministério do Meio Ambiente")
janela.geometry('400x250')
janela.configure(bg='#B3EFB5')
infoJanela = Label (janela, text = "Bem vindo ao Programa de Biometria", font=('georgia',13,'bold'),fg='#182B19',bg='#B3EFB5')
infoJanela.place(x=25, y=15)

infoJanela1 = Label (janela, text = "Por favor, escolha a sua opção de Login", font=('georgia',12),fg='#182B19',bg='#B3EFB5')
infoJanela1.place(x=50, y=45)

botao1 = Button(janela, width=12,height=2, text="Funcionario", command=auth_func,
                font=('georgia',10,'bold'),fg='#182B19',bg='#B3EFB5',bd=3)
botao1.configure(overrelief='sunken')
botao1.place(x=15, y=100)

botao2 = Button(janela, width=12,height=2, text="Diretor", command=auth_diretor,
                font=('georgia',10,'bold'),fg='#182B19',bg='#B3EFB5',bd=3)
botao2.configure(overrelief='sunken')
botao2.place(x=140, y=100)

botao3 = Button(janela, width=12,height=2, text="Ministro", command=auth_ministro,
                font=('georgia',10,'bold'),fg='#182B19',bg='#B3EFB5',bd=3)
botao3.configure(overrelief='sunken')
botao3.place(x=265, y=100)

botao4 = Button(janela, width=6,height=1, text="SAIR", command=quit,
                font=('georgia',10,'bold'),fg='#182B19',background='#B3EFB5')
botao4.place(x=330, y=220)

janela.mainloop()