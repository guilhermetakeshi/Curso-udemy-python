# @property - um getter no modo Pythônico

# getter - um método para obter um atributo

# cor -> get_cor()

# modo pythônico - modo do Python de fazer coisas

# @property é uma propriedade do objeto, ela é um método que se comporta como um
# atributo

# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo

# Código cliente - é o código que usa seu código

# seu código:


'''
class Caneta:
    def __init__(self, cor):
        self.cor = cor
        
    # para evitar o erro nisso, vc coloca um get_cor assim:
    def get_cor(self):
        return self.cor
        
    
##############################################################################

# código cliente

caneta = Caneta('Azul')
#print(caneta.cor)
#print(caneta.cor)
#print(caneta.cor)
#print(caneta.cor)

print(caneta.get_cor())

imagine que cada print é um cliente usando o seu código, desse jeito puro, se vc fizer uma alteração, vai dar
erro nos programas deles pq eles tão pegando o valor direto.

assim, vc usa um get_cor, pq assim, ao inves das pessoas usarem o self.cor "caneta.cor" a pessoa usa
o print(caneta.get_cor()), assim vc protege o seu atributo

'''

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
    
    # em python, podemos usar o @property pq ele é um decorator que faz um método, callable se 
    # comportar como um atributo
    @property
    def cor(self):
        print("Property")
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 123456
        
caneta = Caneta('Azul')


print(caneta.cor)
print(caneta.cor_tampa)

