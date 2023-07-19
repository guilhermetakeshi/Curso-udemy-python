# Relações entre classes: associação, agregação e composição

#                   COMPOSIÇÃO

# Composição é uma especialização da agregação.

# Mas nela, quando o objeto "pai" for apagado, todas as referências dos objetos 
# filhos também são apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
        
    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
        
    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)
    
    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)
    

# nesse caso, eu preciso usar o método Endereco() aqui no cliente pq qnd eu for excluir o cliente
# eu queria que tambem excluisse o endereço, por isso eles devem estar interligados.
# sendo assim, entendemos que o cliente é a classe PAI do endereço

# dessa forma usaremos algo chamado de garbage colector em python

# garbage colector = quando a linguagem vê que não existe mais referência para aquele objeto
# no seu programa, ela apaga o objeto da memória.


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua B', 6745)
endereco_externo = Endereco('Av Saudade', 123213)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.listar_enderecos()
