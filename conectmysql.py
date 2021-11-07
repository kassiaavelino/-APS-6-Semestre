import mysql.connector

# | nome_propri   |  cpf_propri     | tel_propri         | endereco_local |
# | tamanho_local | tipo_agrotoxico | nivel_contaminacao |                |

db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='aps_infos'
)

cursor = db.cursor()

def LerMinistro():
    cursor.execute("SELECT * FROM tb_propriedades")

    result = cursor.fetchall()

    for x in result:
        print(x)

# LerTabela()       

def LerDiretor():
    cursor.execute("SELECT nome_propri, tel_propri, tipo_agrotoxico, nivel_contaminacao FROM tb_propriedades")
    
    result = cursor.fetchall()

    for x in result:
        print(x)

def LerFuncionario():
    cursor.execute("SELECT nome_propri, tel_propri, nivel_contaminacao FROM tb_propriedades")
    
    result = cursor.fetchall()

    for x in result:
        print(x)