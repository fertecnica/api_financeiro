from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime


class FlashScrapper:
    def __init__(self, web_navigator):
        self.web_navigator = web_navigator
        self.driver = self.web_navigator.get_driver()

    def login_process(self):

        # Clica no botão de aceitação de cookies
        self.web_navigator.click_element('//*[@id="modal-termo"]/div/div/div/div/button[1]')

        # Clica no botão de aceitação de cookies
        # self.web_navigator.click_element('//button[contains(text(), "Li e aceito")]')
        
        # Encontra o campo de email e insere o email
        self.web_navigator.fill_input_field('usuarioEmail', 'hassan.primo@fertecnica.net', locator_type=By.ID)
        
        # Clica no botão "PRÓXIMO"
        self.web_navigator.click_element('//*[@id="lookup"]/button')
        
        sleep(20)
        # Clica no botao Fertecnica
        self.web_navigator.click_element('//*[@id="modal-window-organization"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]')
        

        try_end_login = 3
        pass_end_login = False
        
        while try_end_login > 0 and pass_end_login == False:
            try:
                sleep(30)
                # Encontra o campo de senha e insere a senha
                self.web_navigator.clear_input_field('//*[@id="senha"]')
                self.web_navigator.fill_input_field('//*[@id="senha"]', '3823D1C79418@')  
                sleep(5)
                # Clica no botão de login
                self.web_navigator.click_element('//*[@id="login-submit-button"]')
                pass_end_login = True
            except Exception as e:
                print(f'Erro ao finalizar processo de login (pós captcha) -> {e}')
                try_end_login -= 1
                print(f'Restam mais {try_end_login} tentativas')
        
        # Aguarda até que a página de relatórios seja carregada
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'badgeFinanceiroRelatorio')))

    def scrapper_process(self):
        # Abre as configuraçoes do relatorio
        self.web_navigator.click_element('//*[@id="export-excel-container"]/div/small/strong/a')
        
        # Retira o input padrao
        self.web_navigator.clear_input_field('//*[@id="modal-window"]/div/div/div[2]/div/div/div[1]/div/div[1]/input')

        # Obter a data atual
        current_date = datetime.now()

        # Formatar a data no formato desejado
        formatted_date = current_date.strftime('%d/%m/%Y')

        # Encontra o campo de data e define o valor para a data desejada
        self.web_navigator.fill_input_field('//*[@id="modal-window"]/div/div/div[2]/div/div/div[1]/div/div[1]/input', '01/01/2024')
        
        sleep(30)
        # Clica no botão OK para iniciar o download do arquivo
        self.web_navigator.click_element('//button[contains(text(), "OK")]')
        
        print('O download do arquivo deve ter sido iniciado.')
        sleep(30)