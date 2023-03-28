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

def filtrar_preco(produto):
    return produto['preco'] > 100

# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 100
# ]

# filter é um método q faz um filtro, deve receber uma função 
# como parametro(pode ser lambda(que é uma função anonima))

# o segundo parametro deve ser um iteráve (nesse caso, a lista produtos)

novos_produtos = filter(
    # lambda produto: produto['preco'] > 100,
    filtrar_preco,
    produtos
)


print_iter(produtos)
print_iter(novos_produtos)