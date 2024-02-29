from flask import Blueprint
from flash_scrapper import FlashScrapper
from web_navigator import WebNavigator

calls = Blueprint('calls', __name__)

@calls.route('/busca_despesas_flash')
def index():
    # Inicialize o WebNavigator
    navigator = WebNavigator('C:\\Users\\HassanPrimo\\OneDrive - FERTECNICA FERRAMENTAS E EQUIPAMENTOS LTDA\\Aplicativos\\msedgedriver.exe', 'C:\\Users\\HassanPrimo\\Downloads\\recaptcha.crx')

    return 'OK'