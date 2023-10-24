# type: ignore
# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Documentação do Selenium para localização de elementos
# https://selenium-python.readthedocs.io/locating-elements.html

# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    # Cria uma instância de ChromeOptions para configurar as opções do navegador
    chrome_options = webdriver.ChromeOptions()

    # Descomente a linha abaixo para executar o navegador em modo headless (sem interface gráfica)
    # chrome_options.add_argument('--headless')

    # Verifica se foram fornecidas opções personalizadas e as adiciona ao ChromeOptions
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    # Cria um serviço do ChromeDriver com o caminho especificado
    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    # Cria e retorna uma instância do navegador Chrome com o serviço e opções configuradas
    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser

if __name__ == '__main__':
    TIME_TO_WAIT = 10

    # Exemplo de opções que podem ser passadas para a função make_chrome_browser
    options = ()

    # Cria uma instância do navegador Chrome com as opções especificadas
    browser = make_chrome_browser(*options)

    # Abre a página do Google no navegador
    browser.get('https://www.google.com')

    # Espere até encontrar o elemento de entrada de pesquisa
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )
    # Insere texto no campo de pesquisa
    search_input.send_keys('Hello World!')
    search_input.send_keys(Keys.ENTER)

    # Localiza o elemento de resultados
    results = browser.find_element(By.ID, 'search')
    # Localiza todos os links nos resultados
    links = results.find_elements(By.TAG_NAME, 'a')
    # Clica no primeiro link
    links[0].click()

    # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)
