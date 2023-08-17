#Import das bibliotecas
import time
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



#definindo parametros de serviços
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)



#atribuindo funções pasando o xpath
navegador.get ("https://on.fiap.com.br/")
navegador.find_element('xpath','//*[@id="username"]').send_keys("cl2182")
navegador.find_element('xpath','//*[@id="password"]').send_keys("g@br!el#23")
navegador.find_element('xpath','//*[@id="loginbtn"]').click()
navegador.get ("https://on.fiap.com.br/local/fiapdb/admin/add_conteudo_fake.php")


arquivos = ['C://Users//Anubis//OneDrive//Área de Trabalho//Documentos//Aperta o X//Projetos//Python//WEB - Automação//1SI//100 - 1SI - Fase 6 - 2023.csv',
            'C://Users//Anubis//OneDrive//Área de Trabalho//Documentos//Aperta o X//Projetos//Python//WEB - Automação//2SI//100 - 2SI - Fase 6 - 2023.csv',
            'C://Users//Anubis//OneDrive//Área de Trabalho//Documentos//Aperta o X//Projetos//Python//WEB - Automação//3SI//100 - 3SI - Fase 6 - 2023.csv',
            'C://Users//Anubis//OneDrive//Área de Trabalho//Documentos//Aperta o X//Projetos//Python//WEB - Automação//4SI//100 - 4SI - Fase 6 - 2023.csv']


for arquivo in arquivos:
    navegador.find_element('xpath','/html/body/div[5]/div/div/div/section/div/div/form/div[5]/div[2]/div[1]/label/input').click()
    navegador.find_element('xpath','/html/body/div[5]/div/div/div/section/div/div/form/div[6]/div[2]/div[1]/label/input').click()
    navegador.find_element('xpath','/html/body/div[5]/div/div/div/section/div/div/form/div[7]/div[2]/div[1]/label/input').click()
    navegador.find_element('xpath','/html/body/div[5]/div/div/div/section/div/div/form/div[8]/div[2]/div[1]/label/input').click()

    with open(arquivo,'r', encoding= "utf-8" ) as arquivo_csv:
        linhas = csv.reader(arquivo_csv)
        primeira_linha = next(linhas)
        nome_tabela = primeira_linha[0]
        navegador.find_element('xpath', '//*[@id="id_categoryname"]') \
            .send_keys(nome_tabela)

    with open(arquivo,'r', encoding= "utf-8" ) as arquivo_csv:
        linhas = csv.reader(arquivo_csv)
        next(linhas)
        num_linhas = len(list(linhas))
    for i in range(num_linhas - 1):
        botao = navegador.find_element('xpath','//*[@id="id_option_add_fields"]').click()

    with open(arquivo,'r', encoding= "utf-8" ) as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        next(leitor_csv)
        for index, linha in enumerate(leitor_csv):
            conteudo = linha[0]
            caixa_texto = navegador.find_element('xpath', '//*[@id="id_conteudoname_{}"]'.format(index)).send_keys(conteudo)


    time.sleep(5)
    navegador.find_element('xpath','//*[@id="id_submitbutton"]').click()
