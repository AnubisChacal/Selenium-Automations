#Import das bibliotecas
import time
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


#definindo parametros de serviços
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

#atribuindo funções pasando o xpath
navegador.get ("https://on.fiap.com.br/")                                          #= entando no site
navegador.find_element('xpath','//*[@id="username"]').send_keys("cl2182")          #= passando user
navegador.find_element('xpath','//*[@id="password"]').send_keys("g@br!el#23")      #= passando a senha
navegador.find_element('xpath','//*[@id="loginbtn"]').click()                      #= logando
#====================================================================================

links = [
    'https://on.fiap.com.br/course/modedit.php?add=quiz&type=&course=9596&section=0&return=0&sr=0',
      'https://on.fiap.com.br/course/modedit.php?add=quiz&type=&course=9597&section=0&return=0&sr=0',
      'https://on.fiap.com.br/course/modedit.php?add=quiz&type=&course=9598&section=0&return=0&sr=0',
      'https://on.fiap.com.br/course/modedit.php?add=quiz&type=&course=9599&section=0&return=0&sr=0']  # 4SI

arquivos = ['C://Users//Anubis//OneDrive//Área de Trabalho//Documentos//Aperta o X//Projetos//Python//WEB - Automação//1SI//100 - 1SI - Fase 6 - 2023.csv',
            'C://Users//Anubis//OneDrive//Área de Trabalho//Documentos//Aperta o X//Projetos//Python//WEB - Automação//2SI//100 - 2SI - Fase 6 - 2023.csv',
            'C://Users//Anubis//OneDrive//Área de Trabalho//Documentos//Aperta o X//Projetos//Python//WEB - Automação//3SI//100 - 3SI - Fase 6 - 2023.csv',
            'C://Users//Anubis//OneDrive//Área de Trabalho//Documentos//Aperta o X//Projetos//Python//WEB - Automação//4SI//100 - 4SI - Fase 6 - 2023.csv']

for link, arquivo in zip(links, arquivos):
    navegador.get(link)




    # Abrir o arquivo CSV
    with open(arquivo, 'r', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)

        # Pular o cabeçalho se necessário
        next(leitor_csv)

        # Loop pelas linhas do arquivo CSV
        for linha in leitor_csv:
            # Extrair os dados relevantes da linha
            dado = linha[0]

            # Clicar em um elemento
            navegador.find_element(By.CLASS_NAME, "collapseexpand").click()

            # Preencher campos com dados da linha
            navegador.find_element(By.ID, "id_name").send_keys(dado)
            navegador.find_element(By.ID, "id_timeopen_enabled").click()
            navegador.find_element(By.ID, "id_timeclose_enabled").click()
            navegador.find_element(By.ID, "id_is_fast_test").click()


            # Preencher datas e horas de início do curso
            Select(navegador.find_element(By.ID, "id_timeopen_day")).select_by_value("13")
            Select(navegador.find_element(By.ID, "id_timeopen_month")).select_by_value("9")
            Select(navegador.find_element(By.ID, "id_timeopen_year")).select_by_value("2023")
            Select(navegador.find_element(By.ID, "id_timeopen_hour")).select_by_value("0")
            Select(navegador.find_element(By.ID, "id_timeopen_minute")).select_by_value("0")

            # Preencher datas e horas de fim do curso
            Select(navegador.find_element(By.ID, "id_timeclose_day")).select_by_value("25")
            Select(navegador.find_element(By.ID, "id_timeclose_month")).select_by_value("11")
            Select(navegador.find_element(By.ID, "id_timeclose_year")).select_by_value("2023")
            Select(navegador.find_element(By.ID, "id_timeclose_hour")).select_by_value("23")
            Select(navegador.find_element(By.ID, "id_timeclose_minute")).select_by_value("59")

            navegador.find_element(By.ID, "id_submitbutton2").click()

                    # Acessar a página desejada
            navegador.get(link)

            # Executar o restante do seu processo
            # ...

    # Fechar o arquivo CSV
arquivo.close()

# Fechar o driver do Selenium
navegador.quit()




time.sleep(10)

navegador.find_element('xpath','/html/body/div[7]/div/div/div/section/div/div/form/div[2]/a').click()

navegador.find_element('xpath','//*[@id="id_name"]').send_keys("Fast test")