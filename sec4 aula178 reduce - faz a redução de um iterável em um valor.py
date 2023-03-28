# reduce - faz a redução de um iterável em um valor

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

'''
# def funcao_do_reduce(acumulador, produto):
#     print('acumulador', acumulador)
#     print('produto', produto)
#     print()
#     return acumulador + produto['preco']

# o reduce predica de uma função como primeiro argumento, 
# no segundo é a sua lista (produtos nesse caso),
# e o terceirto argumento é o inicial (o total = 0)


total = reduce(
    funcao_do_reduce, produtos, 0
)
'''

total = reduce(
    lambda acumulador, produto: acumulador + produto['preco'],
    produtos,
    0
) 

print('Total é', total)


# total = 0
# for p in produtos:
#     total += p['preco']

# print(total)

# print(sum([p['preco'] for p in produtos]))