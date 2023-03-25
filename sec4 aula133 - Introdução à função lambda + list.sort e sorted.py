# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.

# se a função começar a ficar complexa, n é recomendado usar o lambda

# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True) # o sort, ordena a lista, o (reverse=True) é usado pra
                         # ordenar com ordem contrária
# sorted(lista) / faz a mesma coisa do q o q tá em cima, mas cria uma cópia rasa

# print(lista)

lista = [
     {'nome': 'Luiz', 'sobrenome': 'miranda'},
     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
     {'nome': 'Daniel', 'sobrenome': 'Silva'},
     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
     {'nome': 'Aline', 'sobrenome': 'Souza'},
 ]
 
# o python n sabe ordenar dict (dicionarios), ent devemos ensinar ele a como 
# ordenar o dicionario

# para isso, devemos criar uma função para dizermos como o SORT tem q ordenar
# e devemos passar algum parametro para ele
'''
def ordena(item):
    return item['nome'] #dontro dos [] passamos a chave que queremos ordenar

lista.sort(key=ordena) #dentro dos () devemos passar uma function

for item in lista:
    print(item)
'''
# usando a função lambda para fazer a mesma coisa do q aqui em cima

# lista.sort(key=lambda item: item['nome'])

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted (lista, key=lambda item: item['nome'])
l2 = sorted (lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)


