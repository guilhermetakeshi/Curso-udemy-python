# ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent  # Define o diretório atual como o diretório raiz do script
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'aula_186_diretorio_zip'  # Caminho para o diretório onde os arquivos serão compactados
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'aula186_compactado.zip'  # Caminho para o arquivo ZIP compactado
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'aula186_descompactado'  # Caminho para o diretório onde os arquivos serão descompactados

# Remove diretórios e arquivos existentes, se houver
shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True)
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

# Cria o diretório para a aula
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)

def criar_arquivos(qtd: int, zip_dir: Path):
    # Cria arquivos de texto no diretório especificado
    for i in range(qtd):
        texto = 'arquivo_%s' % i
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo:
            arquivo.write(texto)

# Cria 10 arquivos de texto no diretório CAMINHO_ZIP_DIR
criar_arquivos(10, CAMINHO_ZIP_DIR)

# Criando um arquivo ZIP e adicionando arquivos a ele
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            zip.write(os.path.join(root, file), file)

# Lendo os nomes dos arquivos dentro do arquivo ZIP
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# Extraindo arquivos do arquivo ZIP para um diretório específico
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    zip.extractall(CAMINHO_DESCOMPACTADO)
