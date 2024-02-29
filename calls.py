from flask import Blueprint
from flash_scrapper import FlashScrapper
from web_navigator import WebNavigator

calls = Blueprint('calls', __name__)

@calls.route('/busca_despesas_flash')
def index():
    # Inicialize o WebNavigator
    navigator = WebNavigator('C:\\Users\\HassanPrimo\\OneDrive - FERTECNICA FERRAMENTAS E EQUIPAMENTOS LTDA\\Aplicativos\\msedgedriver.exe', 'C:\\Users\\HassanPrimo\\Downloads\\recaptcha.crx')

    # Acessa a pagina de login do relatorio
    navigator.navigate_to_page('https://app.expenseon.com/admin/login?ReturnURL=/admin/financeiro/relatorio')

    # Inicialize o BankScrapper
    scrapper = FlashScrapper(navigator)

    # Execute o processo de login
    scrapper.login_process()

    # Acessa a pagina de Relatorio
    navigator.navigate_to_page('https://app.expenseon.com/admin/financeiro/relatorio')

    # Execute o processo de scrapping
    scrapper.scrapper_process()

    return 'OK'