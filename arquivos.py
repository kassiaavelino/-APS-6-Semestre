entrada = input("escreva aqui: ")
print('-----')
msg = open('texto.txt','a')
msg.write("\n"+ entrada)
print('salvando arquivo..')
msg.close()
print('-----')
print('fazendo a leitura do arquivo...')
msg = open('texto.txt', 'r')

lendo = msg.read()
print('conteudo do arquivo')
print('-----')
print (lendo)