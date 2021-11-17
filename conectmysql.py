import mysql.connector

# | nome_propri   |  cpf_propri     | tel_propri         | endereco_local |
# | area_local | tipo_agrotoxico | nivel_contaminacao |                |

db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='CityPlace15971',
    database='aps_infos'
)

cursor = db.cursor()

def LerFuncionario():
    cursor.execute("SELECT nome_propri, tel_propri, nivel_contaminacao FROM tb_propriedades")
    result = cursor.fetchall()
  
    print('┌─────────────────────────────────────────────────┐')
    print('│   NOME  │  TELEFONE  │  NIVEL DE CONTAMINAÇÃO   │')
    print('└─────────────────────────────────────────────────┘')
       
    for linha in result:
        for elemento in linha:
            print('',elemento,'', end='')               
        print()
    print()
    
# LerFuncionario()         
    # for linha in result:
    #     conteudo.append(linha[0])
    #     conteudo.append(linha[1])
    #     conteudo.append(linha[2])
    # print(conteudo)
    
    # arquivo = open('arq-aps.txt','a',encoding='utf-8')
    
    # arquivo.writelines(str(conteudo[0]))
    # arquivo.writelines(str(conteudo[1]))
    # arquivo.writelines(str(conteudo[2]))
    # arquivo.close()
    
    # arquivo = open('arq-aps.txt','w', encoding='utf-8')
    # arquivo.write(str(conteudo))
    # arquivo.close()   

def LerDiretor():
    cursor.execute("SELECT nome_propri, tel_propri, area_local, tipo_agrotoxico, nivel_contaminacao FROM tb_propriedades")
    result = cursor.fetchall()
    
    print('┌────────────────────────────────────────────────────────────────────────────┐')
    print('│  NOME  │  TELEFONE  │  AREA  │  TIPO AGROTÓXICO  │  NIVEL DE CONTAMINAÇÃO  │')
    print('└────────────────────────────────────────────────────────────────────────────┘')

    for linha in result:
        for elemento in linha:
            print('',elemento,'', end='')
        print()
        
def LerMinistro():
    cursor.execute("SELECT * FROM tb_propriedades")
    result = cursor.fetchall()
    
    print('┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐')
    print('│      NOME      │      CPF      │      TELEFONE      │      ENDEREÇO      │      AREA      │      TIPO AGROTÓXICO      │      NIVEL DE CONTAMINAÇÃO      │')
    print('└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘')

    for linha in result:
        for elemento in linha:
            print('',elemento,'', end='')
        print()


# print(LerFuncionario(),'\n')

# print(LerDiretor(),'\n')

# print(LerMinistro(),'\n')