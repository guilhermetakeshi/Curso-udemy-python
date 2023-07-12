# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

CAMINHO_ARQUIVO = 'aula207_a.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
p1 = Pessoa('João', 25)
p2 = Pessoa('Maria', 33)
p3 = Pessoa('José', 21)
'''
bd = [p1,p2,p3] - isso daria erro pois o json não sabe como guardar as instâncias de classe p1, p2 e p3
sendo assim, precisamos fazer de outra forma.

uma das possibilidades é fazer:

bd = [vars(p1), vars(p2), vars(p3)]
ou
bd = [p1.__dict__, p2.__dict__, p3.__dict__]
'''

bd = [vars(p1), vars(p2), vars(p3)]
'''
with open (CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
# desse jeito, o arquivo vai fazer o dump sempre pq a aula 207 B está importando as coisas aqui e 
# utilizando isso sempre, para adiarmos a execução, podemos envolver isso numa função
'''
def fazer_dump():
    with open (CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
    
if __name__ == '__main__':
    print('ELE É O __MAIN__')
    fazer_dump()