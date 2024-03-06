from flask import Blueprint
from flash_scrapper import FlashScrapper
from web_navigator import WebNavigator
from data_process import DataProcessor
import os

calls = Blueprint('calls', __name__)

@calls.route('/busca_despesas_flash')
def index():
    # Obtém o caminho do diretório atual
    current_dir = os.path.dirname(os.path.realpath(__file__))

    # Constrói os caminhos completos para o driver e a extensão
    driver_path = os.path.join(current_dir, 'msedgedriver.exe')
    extension_path = os.path.join(current_dir, 'recaptcha.crx')

    # Inicializa o WebNavigator com os caminhos corretos
    navigator = WebNavigator(driver_path, extension_path)
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

    # Define o caminho para a pasta 'downloads' no diretório atual
    download_directory = os.path.join(current_dir, 'downloads')

    # Começa a analisar os dados do arquivo
    processor = DataProcessor(download_directory)
    
    # Arquivo ja tratado
    df = processor.data_organize()

    # Define datas limites para a coluna Data da Despesa
    df = processor.filter_by_date(df, 'Data da Despesa', '2023-07-01', '2023-12-31')
    
    processor.ajustar_colunas_datas(df)

    # Define o caminho para a pasta 'relatorio_flash' no diretório atual
    relatorio_directory = os.path.join(current_dir, 'relatorio_flash')

    # Começa os procedimentos necessarios para converter os dados
    conversor = DataProcessor(relatorio_directory)

    # Converte para json e salva na pasta 'relatorio_flash'
    conversor.salvar_df_como_json(df, 'relatorio')

    return 'OK'