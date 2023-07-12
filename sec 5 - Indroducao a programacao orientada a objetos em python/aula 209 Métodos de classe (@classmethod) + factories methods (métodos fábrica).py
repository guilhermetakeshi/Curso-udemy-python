# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2023 # atributo de classe
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

'''
no método normal de instancia, recebe o self e pode fazer algo, ex:

    def metodo_instancia(self):
        print('Olá, este é o método de instancia)

e para chamar esse método agr, eu tenho q ter uma pessoa:

p1 = Pessoa('João', 34)

e agr chamar o método normal

p1.metodo_instancia() e não precisa passar nada dentro dos parenteses pq o python ja sabe quem é o self

mas imagine que eu tenho um método que eu n quero passar nenhuma instancia, ent usamos o decorator
@classmethod

esse classmethod faz com q eu possa chamar minha classe sem passar o self, mas eu preciso receber 
alguma coisa ali no lugar do self, precisamos receber um parametro que geralmente é a propria classe
geralmente chamamos a classe de cls


    @classmethod
    def metodo_de_classe():
        print('Este é o método de classe')

MAS PRA Q RAIOS EU USARIA O DECORATOR @classmethod?????????????????

temos uma coisa chamada factories method que podemos utilizar para criar um novo objeto com uma coisa
arbitrária, escolhida, hard coded ex:
    
    criar pessoas sempre com 50 anos
    
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
        
p1 = Pessoa('João', 35) isso é a chamada normal
p2 = Pessoa.criar_com_50_anos('Helena') e aqui é a chamada direto no método com 50 anos, hard codado e 
não necessário passar a idade pq sempre vai ser devolvido a idade = 50

print(p2.nome, p2.idade)

exemplo criar alguem anonimo:

    @classmethod
        def criar_sem_nome(cls, idade):
            return cls('Anônimo', idade)

p3 = Pessoa.criar_sem_nome(34)

'''

class Pessoa:
    ano = 2023 # atributo de classe
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônimo', idade)

p3 = Pessoa.criar_sem_nome(34)
print(p3.nome, p3.idade)
