# Atributos de Classes

# o 2023 no return podia ser uma constante para que só tenha um ponto para alterar

# ANO_ATUAL = 2023

# mas eu posso criar um atributo na classe, se o ano atual fosse SOMENTE usada na classe pessoa
# assim, podemos colocar a variavel dentro do escopo da classe, e assim, ela se torna um atributo da classe
# e esse atributo pode ser utilizado fora da classe usando o "Pessoa.ano_atual" que é "nome_da_classe.nome_da_variavel"

class Pessoa:
    ano_atual = 2023
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        # return 2023 - self.idade
        # return ANO_ATUAL - self.idade
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 20)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

'''
# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)
# p1.nome = 'EITA'
# print(p1.idade)
# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'EITA'
# del p1.__dict__['nome']
# print(p1.__dict__)
# print(vars(p1))
# print(p1.outra)
# print(p1.nome)
print(vars(p1))
print(p1.nome)

'''