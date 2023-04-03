# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears

# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

lista_completa = []
lista_refazer = []
 
while True:
    print('Comandos: \n- LISTAR \n- DESFAZER \n- REFAZER \n- SAIR \n')
    tarefa = str(input('Digite uma tarefa ou comando: '))

    print('\nTAREFAS:')
    
    if tarefa in 'listarLISTAR':
        print(*lista_completa)
        print('')
        continue

    elif tarefa in 'DESFAZERdesfazer':
        item_deletado = lista_completa.pop()
        print('A tarefa {} foi removida da lista'.format(item_deletado))
        lista_refazer.append(item_deletado)
        print(lista_completa)
        print('')
        continue
    
    elif tarefa in 'REFAZERrefazer':
        item_deletado = lista_refazer.pop()
        lista_completa.append(item_deletado)
        print(lista_completa)
        print('')
        continue
    else: 
        lista_completa.append(tarefa)

    if tarefa in 'SAIRsair':
        for indice in lista_completa:
            if len(lista_completa) == 0:
                print('Não há tarefas para listar')
            else:
                print(indice, sep='\n', end='\n')
        break
    
    for indice in lista_completa:
        if len(lista_completa) == 0:
            print('Não há tarefas para listar')
        else:
            print(indice, end='\n')
    print('')
            
    
'''
JEITO MOSTRADO NA AULA, ADAPTADO PARA MIM


lista_completa = []
lista_refazer = []

def listar(tarefa):
    print()
    if not tarefa:
        print('Nenhuma tarefa para listar')
        return
    print('TAREFAS:')
    for tarefas in lista_completa:
        print(tarefas)
    print()
        
def desfazer(tarefa, lista_refazer):
    print()
    if not tarefa:
        print('Nenhuma tarefa para desfazer')
        return
    tarefa_excluida = lista_completa.pop()
    print('A tarefa {} foi removida da lista'.format(tarefa_excluida))
    lista_refazer.append(tarefa_excluida)
    print()
    
def refazer(tarefa, lista_refazer):
    print()
    if not tarefa:
        print('Nenhuma tarefa para refazer')
        return
    tarefa_excluida = lista_refazer.pop()
    lista_completa.append(tarefa_excluida)
    print()
    
def adicionar(tarefa, lista_completa):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa')
        return
    lista_completa.append(tarefa)
    print()
 
while True:
    print('Comandos: \n- LISTAR \n- DESFAZER \n- REFAZER \n- SAIR \n')
    tarefa = str(input('Digite uma tarefa ou comando: '))

    if tarefa in 'listarLISTAR':
        listar(tarefa)
        continue

    elif tarefa in 'DESFAZERdesfazer':
        desfazer(tarefa, lista_refazer)
        continue
    
    elif tarefa in 'REFAZERrefazer':
        refazer(tarefa, lista_refazer)
        continue
    else:
        adicionar(tarefa, lista_completa)
    
    if tarefa in 'SAIRsair':
        for indice in lista_completa:
            if len(lista_completa) == 0:
                print('Não há tarefas para listar')
            else:
                lista_completa.pop()
                print(indice, sep='\n', end='\n')
        break
  
'''
        