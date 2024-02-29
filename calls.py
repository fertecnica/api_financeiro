from flask import Blueprint
from flash_scrapper import FlashScrapper
from web_navigator import WebNavigator

calls = Blueprint('calls', __name__)

@calls.route('/busca_despesas_flash')
def index():
    BankScrapper().scrapping_process()
    return 'OK'