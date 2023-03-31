# Problema dos parâmetros mutáveis em funções Python

'''
def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista
    
cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

isso aqui daria erro pois toda vez que eu chamar uma função sem passar um parametro, e esse
parametro é mutável, o python vai sempre reutilizar a mesma lista tanto em cliente1 tanto
para cliente2, assim, o cliente2 vai pegar a lista cliente1 e adicionar com os nomes que 
você passou no cliente2
'''

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

lista1 = []
cliente1 = adiciona_clientes('luiz', lista1)
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)