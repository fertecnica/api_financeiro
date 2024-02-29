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
