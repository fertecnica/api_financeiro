from flask import Blueprint
from flash_scrapper import FlashScrapper
from web_navigator import WebNavigator
from data_process import DataProcessor

calls = Blueprint('calls', __name__)

@calls.route('/busca_despesas_flash')
def index():
    # Inicialize o WebNavigator
    navigator = WebNavigator('msedgedriver.exe', 'recaptcha.crx')

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

    # Começa a analisar os dados do arquivo
    processor = DataProcessor('C:\\Users\\HassanPrimo\\Downloads')  # Substitua por seu caminho
    
    # Arquivo ja tratado
    df = processor.data_organize()

    # Define datas limites para a coluna Data da Despesa
    df = processor.filter_by_date(df, 'Data da Despesa', '2023-07-01', '2023-12-31')


    return 'OK'