def executa(funcao, *args):
    return funcao(*args)
'''
def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica
'''
print(executa(lambda x, y: x + y)) # mesma coisa que a função soma q criei

duplica = executa( lambda m: lambda n: n * m, 2 )

print(duplica(2))

print(executa(lambda x, y: x + y, 2, 3),)

# o lambda é uma função anonima que ta recebendo esses 2 parametros e depois dos dois pontos, vc 
# coloca o que vc quer que esta função retorne, no caso da soma, é o x + y
# apos isso, deve ser informado os valores, que serao colocados como *args na função executa

'''
O lambda x, y:
é a mesma coisa que fazer o "def lambda x, y:"

'''

print(executa(lambda *args: sum(args),1, 2, 3, 4, 5, 6, 7))

