# JSON (JavaScript Object Notation) em Python é um formato de dados leve e fácil de ler, que 
# é amplamente utilizado para representar dados estruturados. JSON é uma notação textual que 
# é comumente usada para trocar dados entre um servidor e um cliente, armazenar configurações 
# e estruturar informações em uma variedade de aplicativos.

# O que é JSON - JavaScript Object Notation
# JSON - JavaScript Object Notation (extensão .json)
# É uma estrutura de dados que permite a serialização
# de objetos em texto simples para facilitar a transmissão de
# dados através da rede, APIs web ou outros meios de comunicação.
# O JSON suporta os seguintes tipos de dados:
# Números: podem ser inteiros ou com ponto flutuante, como 42 ou 3.14
# Strings: são cadeias de caracteres, como "Olá, mundo!" ou "12345"
#    As strings devem ser envolvidas por aspas duplas
# Booleanos: são os valores verdadeiro (true) ou falso (false)
# Arrays: são listas ordenadas de valores, como [1, 2, 3] ou
#    ["Oi", "Olá", "Bom dia"]
# Objetos: são conjuntos de pares chave/valor -> {"nome": "João", "idade": 30}
# null: é um valor especial que representa ausência de valor
#
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null

# json.dumps e json.loads com strings + typing.TypedDict

# Importa o módulo json para trabalhar com JSON em Python
import json
from typing import TypedDict

# Define um TypedDict chamado Movie para representar a estrutura dos dados JSON
class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float

# Define uma string JSON que representa informações sobre um filme
string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''

# Usa json.loads para desserializar a string JSON em um dicionário Python
filme: Movie = json.loads(string_json)

# Converte o dicionário Python de volta para uma string JSON formatada
json_string = json.dumps(filme, ensure_ascii=False, indent=2)

# Imprime a string JSON formatada
print(json_string)

#-----------------------------------------------------------------------------------------------------------------
# aula 290 json.dump e json.load com arquivos

# Importar os módulos necessários
import json
import os

# Definir o nome do arquivo JSON que será criado e lido
NOME_ARQUIVO = 'json aula 288.json'

# Calcular o caminho absoluto do arquivo usando o nome do arquivo atual (__file__)
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),  # Diretório atual do arquivo
        NOME_ARQUIVO
    )
)

# Definir um dicionário Python com informações sobre um filme
filme = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',
    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None  # Orçamento do filme é desconhecido, então definido como None
}

# Abrir o arquivo JSON para escrita ('w') e escrever o dicionário 'filme' nele
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    # A função json.dump escreve o dicionário em formato JSON no arquivo
    # Os argumentos 'ensure_ascii' e 'indent' são usados para controlar a formatação
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

# Abrir o arquivo JSON para leitura ('r') e carregar seu conteúdo em um novo dicionário
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    # A função json.load lê o conteúdo JSON do arquivo e o converte em um dicionário Python
    filme_do_json = json.load(arquivo)

# Imprimir o dicionário resultante (filme_do_json) que foi lido do arquivo JSON
print(filme_do_json)
