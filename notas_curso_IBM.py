'''
Aula sobre APIs I

Application Program Interface - (Interface de Programação de Aplicação)

Neste vídeo, discutiremos as Interfaces de Programa de Aplicação; API, abreviadamente.
Especificamente, discutiremos: O que é uma API, Bibliotecas de API, API REST, incluindo Requisição
e Resposta.

Uma API permite que dois programas de software se comuniquem entre si.
Por exemplo, você tem seu programa, tem alguns dados e tem outros componentes de software.
Você usa a API para se comunicar com a API por meio de entradas e saídas.
Assim como uma função, você não precisa saber como a API funciona, apenas suas entradas e saídas.

O Pandas é na verdade um conjunto de componentes de software, muitos dos quais nem mesmo são escritos em Python.
Você tem alguns dados. Você tem um conjunto de componentes de software.

Usamos a API do Pandas para processar os dados, comunicando-se com os outros Componentes de Software.
Vamos limpar o diagrama. Quando você cria um dicionário e, em seguida, cria
um objeto Pandas com o construtor Dataframe, na linguagem da API, isso é uma "instância".
Os dados no dicionário são passados para a API do Pandas.
Você então usa o dataframe para se comunicar com a API.

Quando você chama o método "head", o dataframe se comunica com a API, exibindo os
primeiras linhas do dataframe. Quando você chama o método "mean", a API irá
calcular a média e retornar os valores.

As APIs REST são outro tipo popular de API; eles permitem que você se comunique pela
internet, permitindo que você aproveite recursos como armazenamento, acesse mais dados,
algoritmos de inteligência artificial e muito mais.

O "RE" significa Representacional, o "S" significa Estado, o "T" significa Transferência.
Nas APIs REST, seu programa é chamado de cliente.

A API se comunica com um serviço da web que você chama pela internet.
Existem regras relacionadas à Comunicação, Entrada ou Requisição e Saída ou Resposta.
Aqui estão alguns termos comuns. Você ou seu código podem ser considerados como um cliente.
O serviço da web é chamado de recurso. O cliente encontra o serviço por meio de um endpoint.
Vamos revisar isso mais na próxima seção. O cliente envia solicitações ao recurso e recebe a resposta do cliente.

Os métodos HTTP são uma maneira de transmitir dados pela internet.
Nós dizemos às APIs REST o que fazer enviando uma solicitação.
A solicitação geralmente é comunicada por meio de uma mensagem HTTP.
A mensagem HTTP geralmente contém um arquivo JSON. Isso contém instruções sobre qual operação
gostaríamos que o serviço executasse. Essa operação é transmitida para o serviço da web
pela internet. O serviço executa a operação.

Da mesma forma, o serviço da web retorna uma resposta por meio de uma mensagem HTTP, onde a
informação geralmente é retornada por meio de um arquivo JSON.
Essas informações são transmitidas de volta para o cliente.
Os dados esportivos estão sempre mudando. Esta é uma excelente aplicação de uma API
pois ela pode ser constantemente atualizada. Vamos usar a API da NBA de Swar Patel.
A API está sempre sendo atualizada a partir de endpoints na NBA.com.

É simples de usar para que você possa se concentrar na tarefa de coletar dados.
Na API da NBA, para fazer uma solicitação para um time específico, é bastante simples.
Não precisamos de um arquivo JSON. Tudo o que precisamos é um ID.
Essas informações são armazenadas localmente na API.

--- import pandas as pd
--- !pip install nba_api
--- from nba_api.stats.static import teams
--- nba_teams = teams.get_teams()
--- nba_teams[:5]

Importamos o módulo "teams". O método "get teams" retorna uma lista de
dicionários, que têm as mesmas chaves, mas os valores dependem do time.
A chave do dicionário "id" tem um identificador exclusivo para cada time como valor.

Para facilitar, podemos converter o dicionário em uma tabela.
Primeiro, criamos a função "one dict" para criar um dicionário.
Usamos as chaves comuns para cada time como chaves, o valor é uma lista; cada elemento da 
lista corresponde aos valores de cada time.

--- def one_dict(list_dict):
---     keys = list_dict[0].keys()
---     out_dict={key:[] for key in keys}
---     for dict_ in list_dict:
---         for key, value in dict_.items():
---             out_dict[key].append(value)
---     return out_dict
--- dict_nba_team = one_dict(nba_teams)

Em seguida, convertemos o dicionário em um dataframe; cada linha contém as informações de um time diferente.

--- df_teams = pd.DataFrame(dict_nba_team)
--- df_teams.head()

Vamos usar o apelido do time para encontrar o ID único.
Podemos encontrar a linha que contém os Warriors da seguinte maneira.

--- df_warriors = df_teams[df_teams['nickname']=='Warriors']
--- print(df_warriors)

O ID é a primeira coluna. Podemos usar a seguinte linha de código para acessar
a primeira coluna do dataframe. 

--- id_warriors = df_warriors[['id']].values[0][0]
--- o retorno será: id_warriors: 1610612744

Agora temos um número inteiro que pode ser usado para solicitar as informações dos Warriors.

A função "League Game Finder" fará uma chamada à API.
O parâmetro "team id nullable" é o ID único dos Warriors.

--- from nba_api.stats.endpoints import leaguegamefinder 
--- gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)

Por baixo dos panos, a API da NBA está fazendo uma solicitação HTTP.
Isso é transmitido para a NBA.com.
As informações solicitadas são fornecidas e transmitidas por meio de uma resposta HTTP.
Isso é atribuído ao objeto "gamefinder".

--- games = gamefinder.get_data_frames()[0] 
--- games.head()

O objeto gamefinder tem um método "get data frame", que retorna um dataframe.
Se visualizarmos o dataframe, veremos que ele contém informações sobre todos os jogos que os Warriors
jogaram. 

A coluna PLUS MINUS contém informaçõessobre a pontuação. Se o valor for negativo, os Warriors perderam
por aqueles pontos; se o valor for positivo, os Warriors ganharam por aquele número de pontos.

A coluna "Matchup" tinha o time com o qual os Warriors estavam jogando; GSW significa Golden State
e TOR significa Toronto Raptors, vs significa que foi um jogo em casa e o símbolo @ significa
um jogo fora de casa. 

Podemos criar dois dataframes, um para os jogos em que os Warriors enfrentaram os Raptors, em casa, e o segundo para os jogos fora de casa.
Podemos plotar a coluna PLUS MINUS para ambos os dataframes.
Vemos que os Warriors jogaram melhor em casa.
'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
Aula sobre APIs II

Neste vídeo, discutiremos as Interfaces de Programa de Aplicação (APIs) que utilizam algum tipo de inteligência artificial. 
Abordaremos os seguintes tópicos:

Transcreveremos um arquivo de áudio usando a API Watson Text to Speech.
Em seguida, traduziremos o texto para um novo idioma usando a API do tradutor de idiomas do Watson.
Na chamada da API, você enviará uma cópia do arquivo de áudio para a API; isso às vezes é chamado uma solicitação de postagem. 
Então a API enviará a transcrição do texto do que o indivíduo está dizendo. 
Nos bastidores, a API está fazendo uma solicitação get.
Em seguida, enviamos o texto que gostaríamos de traduzir para um segundo idioma para uma segunda API.
A API traduzirá o texto e enviará a tradução de volta para você; neste caso, nós traduzimos inglês para espanhol.

Em seguida, fornecemos uma visão geral de: chaves de API e endpoints, Watson Speech to Text e Watson Translate.
Primeiro, revisaremos chaves de API e endpoints, que lhe darão acesso à API.
Uma chave de API é uma forma de acessar a API. É um conjunto exclusivo de caracteres que a API usa para identificar e autorizar você. 
Geralmente, sua primeira chamada à API inclui a chave de API. Isso permitirá seu acesso à API.
Em muitas APIs, você pode ser cobrado por cada chamada. Portanto, assim como sua senha, você deve manter
sua chave de API em segredo.
Um endpoint é simplesmente a localização do serviço. É usado para encontrar a API na
internet, assim como um endereço da web.

Agora, iremos transcrever um arquivo de áudio usando a API de Texto para Fala da Watson.

Transcrição de Áudio com a API de Texto para Fala da Watson:

Primeiro, você deve se inscrever para obter uma chave de API.
Em seguida, faça o download de um arquivo de áudio para o seu diretório.
Importe "SpeechToTextV1" da IBM Watson.

--- pip install --upgrade "ibm-watson>=7.0.0"
--- from ibm_watson import SpeechToTextV1

O endpoint do serviço é determinado pela localização da instância do serviço e é armazenado na variável "URL_s2t".

--- url_s2t = "https://stream.watson platform.net/speech-to-text/api"

Para encontrar a URL correta, consulte as credenciais do serviço.
Faça o mesmo para sua chave de API.

--- iam_apikey_s2t="EOeiZxxxDxV2xxxXXXXXXXXXXXXXXjYen9SKARKW-" 

Crie um objeto Adaptador de Texto para Fala com os parâmetros do endpoint e da chave de API.
Use esse objeto para se comunicar com o serviço de Texto para Fala da Watson.

--- s2t = SpeechToTextV1 (iam_apikey = iam_apikey_s2t, url = url_s2t)

Identifique o caminho do arquivo WAV que deseja converter em texto.
Crie um objeto de arquivo chamado "wav" usando o método "open", definindo o modo como "rb" (leitura em formato binário).

--- filename='hello_this_is_python.wav
--- with open(filename, mode="rb") as wav: 
---     response = s2t.recognize (audio-wav, content_type='audio/wav')

Use o método "recognize" do objeto Adaptador de Texto para Fala para enviar o arquivo de áudio ao serviço.
O parâmetro "audio" é o objeto de arquivo, e o tipo de conteúdo é o formato do arquivo de áudio.
O serviço enviará uma resposta, que é armazenada no objeto "response".
O atributo "result" contém um dicionário Python.

--- response.result
--- este é o dicionário -> {'results': [{'alternatives': [{'confidence': 0.91, 'transcript'] 'hello this is python '}], 'final': True}], 'result_index': 0}

A chave "results" tem uma lista que contém um dicionário. Estamos interessados na chave "transcript".
Podemos atribuí-la à variável "recognized_text" da seguinte forma.

--- recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]

Agora, "recognized_text" contém uma string com o texto transcrito.

--- recognized_text: 'hello this is python'

Agora, vamos ver como traduzir o texto usando o Watson Language Translator.
Primeiro, importamos o Language Translator V3 do ibm_watson.

--- from ibm_watson import LanguageTranslatorV3

Atribuímos o endpoint do serviço à variável “url_lt”. Você pode obter o serviço nas
instruções do laboratório.

--- url_It = 'https://gateway.watsonplatform.net/language-translator/api'

Você precisará de uma chave de API, consulte as instruções do laboratório
sobre como obter a chave de API. Essas solicitações da API requerem a data da
versão, consulte a documentação.

--- apikey_It = 'dU2SaxxxxxxxxxxxxxxxasdfCuasdf"
--- version_It ='2018-05-01'

Criamos um objeto Language Translator chamado “tradutor de idiomas”.

--- language_translator = Language TranslatorV3(iam_apikey=apikey It, url=url_It,version=version_It)

Podemos obter uma lista dos idiomas que o
serviço pode identificar da seguinte forma.

--- language_translator.list_identifiable_languages().get_result()

O método retorna o código do idioma.
Por exemplo, o inglês tem o símbolo “en” e o espanhol tem o símbolo “es”.
Na última seção, atribuímos o texto transcrito à variável "recognized_text".
Podemos usar o método "translate". 
Isso irá traduzir o texto; o resultado é um objeto de Resposta Detalhada.
O parâmetro “text” é o texto. “Model_id” é o tipo de modelo que gostaríamos de usar. 
Neste caso, configuramos como 'en - es' para Inglês para Espanhol.

--- translation_response = language_translator.translate(text = recognized_text, model_id = 'en-es')

Usamos o método "get_result" para obter a tradução do texto e atribuí-lo à variável "translation". 

--- translation = translation_response.get_result()

O resultado é um dicionário que inclui a contagem de palavras e caracteres da tradução. 

--- translation = {'translations': [{'translation': 'Hola, esta es la pitón. '}], 'word_count': 4, 'character_count': 21} 

Podemos obter a tradução e atribuí-la à variável "Spanish_translation" da seguinte forma.

--- spanish_translation = translation['translations'][0]['translation']  
--- spanish_translation = 'Hola, esta es la pitón.'

Usando a variável "Spanish_translation", podemos traduzir o texto de volta para o inglês da seguinte forma.
O resultado é um dicionário. 

--- translation_new = language_translator.translate(text = spanish_translation, model_id = 'es-en').get_result()
--- translation_eng = translation_new['translations'][0]['translation'] 

Podemos obter a string com o texto da seguinte forma. 

--- translation_eng = 'Hey, this is the python.'

Podemos então traduzir o texto para o francês da seguinte forma.

--- French_translation = language_translator.translate(text= translation_eng, model_id='en-fr').get_result()
--- French_translation['translations'][0]['translation'] = "Hé, c'est le python."
'''