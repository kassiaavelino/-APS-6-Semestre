import mysql.connector

db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='testecadastro'
)

cursor = db.cursor()

# criar bd

def CriarBase():
    cursor.execute("CREATE DATABASE testecadastro")
#CriarBase()

# criar tabela

def CriarTabela():
    cursor.execute("CREATE TABLE usuarios (nome TEXT, senha TEXT)")
#CriarTabela()
# inserir

def InserirDados():
    input_nome = input("Digite seu nome: ")
    input_senha = input("Digite sua senha: ")

    comando_sql = "INSERT INTO usuarios (nome,senha) VALUES (%s,%s)"
    valores = (input_nome,input_senha)

    cursor.execute(comando_sql,valores)
    db.commit()

InserirDados()

def LerTabela():
    cursor.execute("SELECT * FROM usuarios")

    result = cursor.fetchall()

    for x in result:
        print(x)

LerTabela()       
