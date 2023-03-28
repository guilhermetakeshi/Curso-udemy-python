# 160. Proposta de 3 exercícios em um
import copy
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos = [
    
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
  
    ]
'''
def ordena(item):
    return item['nome'] #dentro dos [] passamos a chave que queremos ordenar
produtos.sort(key=ordena, reverse=True) #dentro dos () devemos passar uma function q 
#é o 'ordena'
'''

novos_produtos = [
    {**valor, 'preco': round(valor['preco'] * 1.1, 2)}
    for valor in copy.deepcopy(produtos)
]
    
#produtos_ordenados_por_nome = sorted (produtos, key=lambda item: item['nome'])
produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos), key=lambda item : item['nome'])

# produtos_ordenados_por_preco = sorted (produtos, key=lambda item: item['preco'])
# isso fez uma cópia rasa

produtos_ordenados_por_preco = sorted (copy.deepcopy(produtos), key=lambda item: item['preco'])
# isso faz uma cópia profunda

print(*novos_produtos, sep='\n')
print('\n')
print(*produtos_ordenados_por_nome, sep='\n')
print('\n')
print(*produtos_ordenados_por_preco, sep='\n')
    
