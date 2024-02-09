from flask import Blueprint
from bank_scrapper import BankScrapper

calls = Blueprint('calls', __name__)

@calls.route('/busca_despesas_flash')
def index():
    BankScrapper().scrapping_process()
    return 'OK'