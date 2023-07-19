# Relações entre classes: associação, agregação e composição

# AGREGAÇÃO

# Agregação é uma forma mais especializada de associação entre dois ou mais objetos. 

# Cada objeto terá seu ciclo de vida independente.

# Geralmente é uma relação de um para muitos, onde um objeto tem um ou muitos objetos.

# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de outro para fazer determinada tarefa.

# (existem controvérsias sobre as definições de agregação).

class Carrinho:
    def __init__(self):
        self._produtos = []
    
    def preco_total(self):
            return f'o preço total do carrinho é {sum([p.preco for p in self._produtos])} reais'
    
    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        
    def listar_produtos(self):
        print('')
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print('')
    
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
carrinho = Carrinho()
p1 , p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)

carrinho.inserir_produtos(p1, p2)

carrinho.listar_produtos()

# a relação de agregação acontece pq o carrinho existe independente do produto e vice-versa, mas ambos não
# funcionam tão bem sozinhos pq eles precisam de uma relação

print(carrinho.preco_total())