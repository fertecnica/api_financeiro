from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BankScrapper:
    def __init__(self, web_navigator):
        self.web_navigator = web_navigator
        self.driver = self.web_navigator.get_driver()

    def login_process(self):
        # Clica no botão de aceitação de cookies
        self.web_navigator.click_element('//button[contains(text(), "Li e aceito")]')
        
        # Encontra o campo de email e insere o email
        self.web_navigator.fill_input_field('usuarioEmail', 'hassan.primo@fertecnica.net', locator_type=By.ID)
        
        # Clica no botão "PRÓXIMO"
        self.web_navigator.click_element('//*[@id="lookup"]/button')
        
        time.sleep(20)
        
        # Clica no botao Fertecnica
        self.web_navigator.click_element('//*[@id="modal-window-organization"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]')
        
        time.sleep(5)
        # Encontra o campo de senha e insere a senha
        self.web_navigator.fill_input_field('//*[@id="senha"]', '3823D1C79418@')
        
        time.sleep(30)
        # Clica no botão de login
        self.web_navigator.click_element('//*[@id="login-submit-button"]')
        
        # Aguarda até que a página de relatórios seja carregada
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'badgeFinanceiroRelatorio')))
