
# Este código em Python envolve operações de gerenciamento de arquivos e diretórios utilizando módulos 
# como os e shutil. Vou dividir o código em temas e fornecer comentários sobre cada parte.

# Tema 1: Limpar o Terminal

import os
os.system('clear')
os.system('echo "Hello world"')

#Nesta parte, o código utiliza o módulo os para executar comandos no terminal. 
# O comando clear é usado para limpar o terminal em sistemas Linux e Mac, enquanto echo "Hello world" 
# exibe "Hello world" no terminal. Isso é útil para fins de limpeza e exibição de mensagens.

# Tema 2: Trabalhar com Caminhos de Arquivos

import os
caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
diretorio, arquivo = os.path.split(caminho)
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(caminho)
print(os.path.basename(caminho))
print(os.path.basename(diretorio))
print(os.path.dirname(caminho))

# Nesta parte, o código demonstra o uso do módulo os.path para manipular caminhos de arquivos. 
# Ele cria um caminho, divide-o em diretório e nome de arquivo, extrai a extensão do arquivo e imprime 
# várias partes do caminho. Isso é útil para trabalhar com caminhos de forma independente do sistema operacional.

# Tema 3: Navegar em Diretórios

import os
caminho = os.path.join('/Users', 'luizotavio', 'Desktop', 'EXEMPLO')
for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)
    if not os.path.isdir(caminho_completo_pasta):
        continue
    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)
        
# Nesta parte, o código utiliza o módulo os para listar o conteúdo de um diretório especificado. 
# Ele itera sobre as pastas e, se encontrar subdiretórios, lista também os arquivos dentro deles. 
# Isso é útil para navegar e explorar a estrutura de diretórios.

# Tema 4: Navegar em Diretórios de Forma Recursiva

import os
caminho = os.path.join('/Users', 'luizotavio', 'Desktop', 'EXEMPLO')
for root, dirs, files in os.walk(caminho):
    ...
    # Processamento recursivo aqui
    
# Nesta parte, o código utiliza a função os.walk para percorrer uma estrutura de diretórios de forma recursiva. 
# Ele gera uma sequência de tuplas contendo informações sobre os diretórios e arquivos encontrados em cada nível 
# da árvore de diretórios. Isso é útil para realizar operações em todos os arquivos e diretórios de maneira recursiva.

# Tema 5: Obter o Tamanho de Arquivos

import os
stats = os.stat(caminho_completo_arquivo)
tamanho = stats.st_size

# Nesta parte, o código utiliza o módulo os para obter informações estatísticas sobre um 
# arquivo, incluindo seu tamanho em bytes. A função os.stat é usada para isso. O tamanho é então 
# formatado em uma representação mais legível com a função formata_tamanho.

# Tema 6: Copiar Arquivos de um Diretório para Outro

import os
import shutil
shutil.copy(caminho_arquivo, caminho_novo_arquivo)

# Nesta parte, o código utiliza o módulo shutil para copiar arquivos de uma pasta para outra. 
# A função shutil.copy é usada para realizar a cópia. Isso é útil para fazer backup ou mover arquivos.

# Tema 7: Apagar, Copiar, Mover e Renomear Pastas

import os
import shutil
shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
shutil.rmtree(NOVA_PASTA, ignore_errors=True)

# Nesta parte, o código utiliza o módulo shutil para realizar várias operações em pastas, como 
# apagar, copiar, mover e renomear. Por exemplo, shutil.rmtree é usado para apagar uma pasta recursivamente. 
# É importante ter cuidado ao executar essas operações, especialmente a exclusão, pois os dados podem ser perdidos permanentemente.

# Este código é um exemplo útil para demonstrar muitas funcionalidades relacionadas à manipulação de arquivos 
# e diretórios em Python. Certifique-se de entender completamente as operações realizadas antes de aplicá-las 
# em seu próprio código, especialmente aquelas que podem modificar ou excluir dados.