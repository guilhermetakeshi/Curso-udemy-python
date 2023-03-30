# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)

# Modos:
# r - read (leitura), w - write (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)

caminho_arquivo = 'aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
# no open, vc tem q passar o primeiro parametro como o nome do arquivo e o segundo parametro
# com o q vc quer fazer com o arquivo (passa o modo, nesse caso o (w - write (escrita)))
#
# arquivo.close() isso fecha o arquivo

# podemos usar o "with open()" para fazer a msm coisa, só que quando usamos o with, 
# não precisamos do "close()" pq ele já fecha o arquivo automaticamente

with open(caminho_arquivo, 'w') as arquivo:
    print('Olá mundo')
    print('Arquivo vai ser fechado')

