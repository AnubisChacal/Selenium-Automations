#Import das bibliotecas
import time
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


#definindo parametros de serviços
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

#atribuindo funções pasando o xpath
navegador.get ("https://on.fiap.com.br/")                                          #= entando no site
navegador.find_element('xpath','//*[@id="username"]').send_keys("cl2182")          #= passando user
navegador.find_element('xpath','//*[@id="password"]').send_keys("g@br!el#23")      #= passando a senha
navegador.find_element('xpath','//*[@id="loginbtn"]').click()                      #= logando
#====================================================================================


links = ['https://on.fiap.com.br/course/edit.php?category=1541&returnto=catmanage',#1SI
         'https://on.fiap.com.br/course/edit.php?category=1542&returnto=catmanage',#2SI
         'https://on.fiap.com.br/course/edit.php?category=1543&returnto=catmanage',#3SI
         'https://on.fiap.com.br/course/edit.php?category=1544&returnto=catmanage',]#4SI

arquivos = ['C://Users//Anubis//OneDrive//Área de Trabalho//Documentos//Aperta o X//Projetos//Python//WEB - Automação//criar_curso//1SI//100GRAD1SIFASE6-2023.csv',#1SI
            'C://Users//Anubis//OneDrive//Área de Trabalho//Documentos//Aperta o X//Projetos//Python//WEB - Automação//criar_curso//2SI//100GRAD2SIFASE6-2023.csv',#2SI
            'C://Users//Anubis//OneDrive//Área de Trabalho//Documentos//Aperta o X//Projetos//Python//WEB - Automação//criar_curso//3SI//100GRAD3SIFASE6-2023.csv', #3SI
            'C://Users//Anubis//OneDrive//Área de Trabalho//Documentos//Aperta o X//Projetos//Python//WEB - Automação//criar_curso//4SI//100GRAD4SIFASE6-2023.csv', ]#4SI

for link, arquivo in zip(links, arquivos):
    navegador.get(link)


    #inicio do curso
    Select(navegador.find_element(By.ID, 'id_startdate_day')).select_by_value('13')   # = Dia
    Select(navegador.find_element(By.ID, 'id_startdate_month')).select_by_value('9')  # = Mês
    Select(navegador.find_element(By.ID, 'id_startdate_year')).select_by_value('2023')  # = Ano
    
    Select(navegador.find_element(By.ID, 'id_startdate_hour')).select_by_value('0')    #= Horas
    Select(navegador.find_element(By.ID, 'id_startdate_minute')).select_by_value('0')   #= Minutos
    #=====================================================================================
    #fim do curso
    Select(navegador.find_element(By.ID, 'id_enddate_day')).select_by_value('25')
    Select(navegador.find_element(By.ID, 'id_enddate_month')).select_by_value('11')
    Select(navegador.find_element(By.ID, 'id_enddate_year')).select_by_value('2025')
    Select(navegador.find_element(By.ID, 'id_enddate_hour')).select_by_value('23')
    Select(navegador.find_element(By.ID, 'id_enddate_minute')).select_by_value('59')
    
    #=====================================================================================
    
    
    #regra
    
    Select(navegador.find_element(By.ID, 'id_regra')).select_by_value('2')
    
    #=========================================
    
    
    #pula a primeira linha e armazena a segunda linha em uma variável
    with open(arquivo, 'r', encoding="utf-8") as arquivo_csv:
        linhas = csv.reader(arquivo_csv)
    
        next(linhas)
        segunda_linha = next(linhas)
        nome_tabela = segunda_linha[0]
        navegador.find_element('xpath', '//*[@id="id_fullname"]') \
            .send_keys(nome_tabela)
        
    
    with open(arquivo, 'r', encoding="utf-8") as arquivo_csv:
        linhas = csv.reader(arquivo_csv)
    
        primeira_linha = next(linhas)
        nome_tabela = primeira_linha[0]
        navegador.find_element('xpath', '/html/body/div[5]/div/div/div/section/div/div/form/fieldset[1]/div/div[2]/div[2]/input') \
            .send_keys(nome_tabela)
        navegador.find_element('xpath', '/html/body/div[5]/div/div/div/section/div/div/form/fieldset[1]/div/div[7]/div[2]/input') \
            .send_keys(nome_tabela)
    
    
    
    navegador.find_element('xpath','/html/body/div[5]/div/div/div/section/div/div/form/div[3]/div[2]/div[1]/span/input').click()