# Exercício com classes

# 1 - Crie uma classe Carro (Nome)

# 2 - Crie uma classe Motor (Nome)

# 3 - Crie uma classe Fabricante (Nome)

# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros

# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros

# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor
        
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
        

class Motor:
    def __init__(self, nome):
        self.nome = nome 
    
class Fabricante:
    def __init__(self, nome):
        self.nome = nome

skyline = Carro('Skyline GTR-R34')
v8 = Motor('V8 turbo')
honda = Fabricante('Honda')

skyline.fabricante = honda
skyline.motor = v8

print(f'O Carro {skyline.nome} é do fabricante: {skyline.fabricante.nome}, com Motor: {skyline.motor.nome}\n')
#print(skyline.nome, skyline.fabricante.nome, skyline.motor.nome)

r8 = Carro('R8')
v6_biturbo = Motor('V6 Biturbo')
audi = Fabricante('Audi')

r8.fabricante = audi
r8.motor = v6_biturbo

print(f'O Carro {r8.nome} é do fabricante: {r8.fabricante.nome}, com Motor: {r8.motor.nome}\n')



