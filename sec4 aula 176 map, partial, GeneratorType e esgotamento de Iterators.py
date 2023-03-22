# map, partial, GeneratorType e esgotamento de Iterators

from functools import partial

# partial é uma funcao que vai receber outra funcao

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
    return round((valor * porcentagem), 2)

aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem = 1.1)
'''
novos_produtos = [{**produto, 'preco':aumentar_dez_porcento(produto['preco'])} 
    for produto in produtos]
    
isso pode ser feito através da funcao map

ela precisa de outra funcao, e essa outra funcao é quem vai fazer a tarefa que voce quiser fazer
'''

def muda_preco_de_produto(produto):
    return {**produto, 'preco':aumentar_dez_porcento(produto['preco'])}

novos_produtos = map(muda_preco_de_produto, produtos)

# o primeiro parametro deve ser uma função
# o segundo parametro deve ser um iterável

# o "muda_preco_de_produto" é a funcao e o q vc quer q ela faça, 
# o "produtos" é a lista em si, com a parte do "for produto in produtos"

print_iter(novos_produtos)

print(list(map(lambda x: x * 3, [1, 2, 3, 4])))
# usando a funcao lambda dentro do map

