from data_tools import DataTools
import pandas as pd

class DataProcessor:
    def __init__(self, download_path):
        self.download_path = download_path
        self.tools = DataTools(download_path)

    # Organiza e trata a informaçao
    def data_organize(self):
        # Obtém o nome do último arquivo baixado
        latest_file = self.tools.get_latest_file()

        # Lendo o arquivo excel referente ao relatorio flash
        df = pd.read_excel(f'{self.download_path}\\{latest_file}')

        # Elimina as colunas vazias
        df = df.dropna(how='all', axis=1)

        #Coluna de naturezas
        df.rename(columns={"Código Conta Contábil": "Natureza"}, inplace=True)

        # Adicionando uma nova coluna 'Valor Excedente' ao DataFrame original
        df['Valor Excedente'] = df.apply(lambda row: row['Valor'] - (150 if row['Categoria'] == 'Hospedagem' else
                                                             30 if row['Categoria'] == 'Lavagem de veículos' else
                                                             35 if row['Categoria'] == 'Refeição' else
                                                             40 if row['Categoria'] == 'Estacionamento' else
                                                             0 if row['Categoria'] in ['Despesas ambulatoriais ou medicações', 'Estacionamento', 'Refeição', 'Lavagem de veículos', 'Hospedagem'] else
                                                             row['Valor']), axis=1)

        # Substituindo valores negativos por 0 na coluna 'Valor Excedente'
        df['Valor Excedente'] = df['Valor Excedente'].apply(lambda x: x if x > 0 else 0)

        return df
