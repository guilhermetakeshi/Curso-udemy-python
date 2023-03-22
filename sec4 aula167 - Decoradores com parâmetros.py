# Decoradores com parâmetros

# a função decoradora é usada para criar funções (fabrica de funções)
# 

def fabrica_de_decoradores(a=None, b=None, c=None):
    # "a=None, b=None, c=None" são parametros do decorador
    def fabrica_de_funcoes(func): # é o decorador em si e por padrão, tem que receber uma função
        print('Decoradora 1')
        # a função aninhada pode receber o que eu quiser/precisar
        def aninhada(*args, **kwargs): # a aninhada é a mais interna e vai substituir 
        #a função real (a soma na linha 21)
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes


@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y


decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y) # os Parâmetros são o "x,y" e o retorno da função 
# lambda é o que tá depois dos dois pontos

# função lambda funções que o usuário não precisa definir, ou seja, não vai precisar 
# escrever a função e depois utilizá-la dentro do código.

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)


