# 174. Combinations, Permutations e Product - Itertools

# Combinations, Permutations e Product - Itertools

# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
    ]
    
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster'],
    ]

#print(*list(combinations(pessoas,2)), sep='\n')

def print_iter(iterator):
    print(*list(iterator),sep='\n')
    print()
    
#print(combinations(pessoas,2)) # combinação de "pessoas" em grupos de 2
# print_iter(combinations(pessoas,2)) # devolve combinações únicas onde a ordem n importa

# print_iter(permutations(pessoas,2)) # devolve TODAS as combinações, inclusive as repetições
# ex: 'João', 'Joana' e 'Joana', 'João' (são os mesmos valores e pela ordem estar diferente, 
# a permutations entende como nova combinação)

print_iter(product(*camisetas, pessoas))
# utilizei o * para desempacotar a lista camisetas e após a vírgula passo a lista pessoas para
# fazer ele associar as especificações da camisa com as pessoas
