#As aréas em trasejados estão assim por segurança

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
navegador.find_element('xpath','//*[@id="username"]').send_keys("-----")          #= passando user
navegador.find_element('xpath','//*[@id="password"]').send_keys("-----")      #= passando a senha
navegador.find_element('xpath','//*[@id="loginbtn"]').click()                      #= logando
#====================================================================================


# Listas 
links = ['https://-----/course/edit.php?category=-----&returnto=catmanage',
         'https://-----/course/edit.php?category=-----&returnto=catmanage',
         'https://-----/course/edit.php?category=-----&returnto=catmanage',
         'https://-----/course/edit.php?category=-----returnto=catmanage',]

arquivos = ['C://Users//-----//OneDrive//Área de Trabalho//Documentos//-----//Projetos//Python//WEB - Automação//criar_curso//-----//-----',
            'C://Users//-----//OneDrive//Área de Trabalho//Documentos//-----//Projetos//Python//WEB - Automação//criar_curso//-----//-----',
            'C://Users//-----//OneDrive//Área de Trabalho//Documentos//-----//Projetos//Python//WEB - Automação//criar_curso//-----//-----',
            'C://Users//-----//OneDrive//Área de Trabalho//Documentos//-----//Projetos//Python//WEB - Automação//criar_curso//-----//-----', ]


#Preenchimento de infos das paginas por meio de expreções expecificas e infos dos arquivos das listas 
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
    
    
    #Salva e retorna o loop até o termino das listas
    navegador.find_element('xpath','/html/body/div[5]/div/div/div/section/div/div/form/div[3]/div[2]/div[1]/span/input').click()
