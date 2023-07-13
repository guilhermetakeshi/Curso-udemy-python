# @property + @setter - getter e setter no modo Pythônico

# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo

# Atributos que começar com um ou dois underlines não devem ser usados fora da classe.

# O setter é um método utilizado para que voce configure determinado atributo
# O setter precisa de algum lugar pra salvar o valor


class Caneta:
    def __init__(self, cor):
        # private protected
        self.cor = cor
        self._cor_tampa = None
    
    @property
    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor
    # toda vez que a gente ver o _ antes de qualquer nome de atributo, significa por convenção que
    # ele não deve ser utilizado por outros desenvolvedores. É como se fosse um sinal de alerta 
    # de "NÃO USE ESSE ATRIBUTO", ele é um atributo protegido pela classe
    
    @cor.setter
    def cor(self, valor):
        print('AGORA ESTOU NO SETTER')
        self._cor = valor
        return
    
    # o setter tbm é um método q tem q ter o self e algum valor
    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul')
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Azul'
print(caneta.cor)
print(caneta.cor_tampa)

