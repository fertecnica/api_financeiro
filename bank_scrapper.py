from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
 
class BankScrapper:
 
    def __init__(self) -> None:
        pass
 
    def scrapping_process(self):
        # Cria um objeto de opções para o Edge
        edge_options = Options()
       
        # Cria um objeto de serviço e especifica o caminho para o driver do Edge
        edge_service = Service('C:\\Users\\HassanPrimo\\OneDrive - FERTECNICA FERRAMENTAS E EQUIPAMENTOS LTDA\\Aplicativos\\msedgedriver.exe')
       
        # Inicializa o driver do Edge com as opções e o serviço especificados
        driver = webdriver.Edge(service=edge_service, options=edge_options)
       
        # Acessa a página de login
        driver.get('https://app.expenseon.com/admin/login?ReturnURL=/admin/financeiro/relatorio')
       
        # Aguarda até que o botão de aceitação de cookies esteja visível
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//button[contains(text(), "Li e aceito")]')))
       
        # Clica no botão de aceitação de cookies
        driver.find_element(By.XPATH, '//button[contains(text(), "Li e aceito")]').click()
       
        # Aguarda até que o campo de email esteja visível
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'usuarioEmail')))
       
        # Encontra o campo de email e insere o email
        driver.find_element(By.ID, 'usuarioEmail').send_keys('hassan.primo@fertecnica.net')
       
        # Aguarda até que o botão "PRÓXIMO" esteja visível
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="lookup"]/button')))
       
        # Clica no botão "PRÓXIMO"
        driver.find_element(By.XPATH, '//*[@id="lookup"]/button').click()
       
        # Aguarda até que o campo de senha esteja visível
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'usuarioSenha')))
       
        # Encontra o campo de senha e insere a senha
        driver.find_element(By.ID, 'usuarioSenha').send_keys('3823D1C79418@')  # Substitua 'your_password_here' pela sua senha real
       
        # Clica no botão de login
        driver.find_element(By.NAME, 'login').click()
       
        # Aguarda até que a página de relatórios seja carregada
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'badgeFinanceiroRelatorio')))
       
        # Navega diretamente para a página de relatórios
        driver.get('https://app.expenseon.com/admin/financeiro/relatorio')
       
        # Aguarda até que o campo de data esteja visível
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'dt_inicio')))
       
        # Encontra o campo de data e define o valor para a data desejada
        driver.find_element(By.NAME, 'dt_inicio').clear()
        driver.find_element(By.NAME, 'dt_inicio').send_keys('01/07/2023')
       
        # Aguarda até que o botão OK esteja visível
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//button[contains(text(), "OK")]')))
       
        # Clica no botão OK para iniciar o download do arquivo
        btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div/div[1]/fieldset/button').click()
        print(f'Resposta -> {btn}')