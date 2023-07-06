#modificação da aula 193 para salvar a lista de tarefas em JSON

import json
import os

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
'''    
def ler(lista_completa, caminho_arquivo):
    dados = lista_completa
    with open(caminho_arquivo, 'r', encoding='utf8') as arquivo
'''

def ler(lista_completa, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe!!')
        salvar(lista_completa, caminho_arquivo)
    return dados

def salvar(lista_completa, caminho_arquivo):
    dados = lista_completa
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(lista_completa, arquivo, indent=2, ensure_ascii=False)
    return dados

CAMINHO_ARQUIVO = 'aula193.json'
lista_completa = ler([],CAMINHO_ARQUIVO)
lista_refazer = []
    
while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(lista_completa),
        'desfazer': lambda: desfazer(lista_completa, lista_refazer),
        'refazer': lambda: refazer(lista_completa, lista_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, lista_completa),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()
    salvar(lista_completa, CAMINHO_ARQUIVO)

'''
while True:
    print('Comandos: \n- LISTAR \n- DESFAZER \n- REFAZER \n- SAIR \n')
    tarefa = str(input('Digite uma tarefa ou comando: '))

    if tarefa in 'LISTARlistar':
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
