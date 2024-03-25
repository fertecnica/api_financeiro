from flask import Blueprint, after_this_request
from flash_scrapper import FlashScrapper
from web_navigator import WebNavigator
from data_process import DataProcessor
import os
import json

calls = Blueprint('calls', __name__)

@calls.route('/busca_despesas_flash')
def index():
    # Obtém o caminho do diretório atual
    current_dir = os.path.dirname(os.path.realpath(__file__))

    # Constrói os caminhos completos para o driver e a extensão
    driver_path = os.path.join(current_dir, 'msedgedriver')
    extension_path = os.path.join(current_dir, 'recaptcha.crx')

    # Inicializa o WebNavigator com os caminhos corretos
    navigator = WebNavigator(driver_path, extension_path)
    # Acessa a pagina de login do relatorio
    navigator.navigate_to_page('https://app.expenseon.com/admin/login?ReturnURL=/admin/financeiro/relatorio')

    try_init_scrapper = 3
    pass_init_scrapper = False

    while try_init_scrapper > 0 and pass_init_scrapper == False:
        try:
            # Inicialize o BankScrapper
            scrapper = FlashScrapper(navigator)
            pass_init_scrapper = True
        except Exception as e:
            print(f'Erro ao inicializar página de scrapping -> {e}')
            try_init_scrapper -= 1
            print(f'Restam mais {try_init_scrapper} tentativas')
    
    if pass_init_scrapper == False:
        return 'error'


    scrapper.login_process()

    # Acessa a pagina de Relatorio
    navigator.navigate_to_page('https://app.expenseon.com/admin/financeiro/relatorio')

    try_scrapping_process = 3
    pass_scrapping_process = False

    while try_scrapping_process > 0 and pass_scrapping_process == False:
        try:
            # Execute o processo de scrapping
            scrapper.scrapper_process()
            pass_scrapping_process = True
        except Exception as e:
            print(f'Erro ao realizar processo de scrapping -> {e}')
            try_scrapping_process -= 1
            print(f'Restam mais {try_scrapping_process} tentativas')
    
    if pass_scrapping_process == False:
        return 'error'

    # Define o caminho para a pasta 'downloads' no diretório atual
    download_directory = os.path.join(current_dir, 'downloads')

    try_file_process = 3
    pass_file_process = False

    while try_file_process > 0 and pass_file_process == False:
        try:
            # Começa a analisar os dados do arquivo
            processor = DataProcessor(download_directory)
            pass_file_process = True
        except Exception as e:
            print(f'Erro ao realizar processamento de dados -> {e}')
            try_file_process -= 1
            print(f'Restam mais {try_file_process} tentativas')
    
    if pass_file_process == False:
        return 'error'
    
    try_data_organization = 3
    pass_data_organization = False

    while try_data_organization > 0 and pass_data_organization == False:
        try:
            # Arquivo ja tratado
            df = processor.data_organize()

            # Define datas limites para a coluna Data da Despesa
            df = processor.filter_by_date(df, 'Data de aprovação relatório', '2024-01-01', '2024-12-31')
    
            processor.ajustar_colunas_datas(df)
            pass_data_organization = True
        except Exception as e:
            print(f'Erro ao realizar organização dos dados -> {e}')
            try_data_organization -= 1
            print(f'Restam mais {try_data_organization} tentativas')

    try_data_processor = 3
    pass_data_processor = False

    while try_data_processor > 0 and pass_data_processor == False:
        try:
            # Define o caminho para a pasta 'relatorio_flash' no diretório atual
            relatorio_directory = os.path.join(current_dir, 'relatorio_flash')

            # Começa os procedimentos necessarios para converter os dados
            conversor = DataProcessor(relatorio_directory)

            # Converte para json e salva na pasta 'relatorio_flash'
            conversor.salvar_df_como_json(df, 'relatorio.json')
            
            with open(os.path.join(current_dir, 'relatorio_flash/relatorio.json'), 'r') as arquivo:
                dados = json.load(arquivo)
            print(dados)
            pass_data_processor = True
        except Exception as e:
            print(f'Erro ao realizar processamento dos dados')
            try_data_processor -= 1
            print(f'Restam mais {try_data_processor} tentativas')

    @after_this_request
    def remove_file(response):
        try:
            os.remove(os.path.join(current_dir, f'downloads/{processor.tools.get_latest_file()}'))
            os.remove(os.path.join(current_dir, f'relatorio_flash/relatorio.json'))
            #new_file.close()
        except Exception as error:
            print(f'Erro ao apagar arquivos depois da request -> {error}')
        return response

    return 'OK'