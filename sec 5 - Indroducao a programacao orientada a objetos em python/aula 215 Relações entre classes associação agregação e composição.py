# Relações entre classes: associação, agregação e composição

# Associação é um tipo de relação onde os objetos estão ligados dentro do sistema.

# Essa é a relação mais comum entre objetos e tem subconjuntos como 
# agregação e composição (que veremos depois).

# Geralmente, temos uma associação quando um objeto tem um atributo que referencia outro objeto.

# A associação não especifica como um objeto controla o ciclo de vida de outro objeto.

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

# um Escritor precisa de uma ferramenta de escrever, mas como fazemos essa associação?
# para isso, criamos uma property e um setter ferramenta (a gente cria o atributo ferramenta)
    
    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta
    

class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome
        
    def escrever(self):
        return f'{self.nome} está escrevendo'
        
escritor = Escritor('Guilherme')
caneta = FerramentaDeEscrever('caneta BIC')

# e para associar os 2 objetos, a gente faz assim:

escritor.ferramenta = caneta

# isso liga uma coisa na outra e assim, podemos escrever de ambas as formas:

print(caneta.escrever())
print(escritor.ferramenta.escrever())

# mas pode ser que o escritor tenha mais de uma opção de ferramenta

maquina_de_escrever = FerramentaDeEscrever('Máquina')
escritor.ferramenta = maquina_de_escrever

print(caneta.escrever())
print(maquina_de_escrever.escrever())
print(escritor.ferramenta.escrever())