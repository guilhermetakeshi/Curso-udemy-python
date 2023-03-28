# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def criar_funcao(funcao, x): #aqui vc passa o q ta do lado de
# "criar_funcao(soma" como sendo o x
    def interna(y): #interna é uma função que simula ser a função "funcao"
    # e o y aqui vai ser pego quando vc der o print(multiplica_por_dez(y))
        return funcao(x,y)
    return interna  # sem os parenteses pq vc n quer q execute nesse momento,
                    # vc so quer q execute qnd chamar no print

soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)
print(multiplica_por_dez(5)) # aqui no lugar do 5, é aonde vai ser jogado como Y
print(soma_com_cinco(10))


