from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebNavigator:
    def __init__(self, driver_path, extension_path):
        edge_options = Options()
        edge_service = Service(driver_path)

        # Adiciona a extensao .crx
        edge_options.add_extension(extension_path)

        self.driver = webdriver.Edge(service=edge_service, options=edge_options)

    # Navega para a página da web especificada
    def navigate_to_page(self, url):
        self.driver.get(url)

    # Retorna o driver do navegador atualmente em uso
    def get_driver(self):
        return self.driver

    # Aguarda até que o elemento esteja visível e então clica nele
    def click_element(self, locator, locator_type=By.XPATH, wait_time=10):
        element = WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located((locator_type, locator)))
        element.click()

    # Aguarda até que o campo de entrada esteja visível e então preenche com o texto fornecido
    def fill_input_field(self, locator, input_text, locator_type=By.XPATH, wait_time=10):
        input_field = WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located((locator_type, locator)))
        input_field.send_keys(input_text)