from data_tools import DataTools
import pandas as pd
from datetime import datetime
import os
import json

class DataProcessor:
    def __init__(self, caminho_utilizado):
        self.caminho_utilizado = caminho_utilizado
        self.tools = DataTools(caminho_utilizado)

    # Organiza e trata a informaçao
    def data_organize(self):
        # Obtém o nome do último arquivo baixado
        latest_file = self.tools.get_latest_file()

        # Lendo o arquivo excel referente ao relatorio flash
        df = pd.read_excel(f'{self.caminho_utilizado}\\{latest_file}')

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
                                                             row['Valor']), axis=1
                                                            )

        # Substituindo valores negativos por 0 na coluna 'Valor Excedente'
        df['Valor Excedente'] = df['Valor Excedente'].apply(lambda x: x if x > 0 else 0)

        # Seleciona apenas as colunas específicas para conversão
        colunas_para_converter = ['CPF Solicitante', 
                                  'CNPJ Filial Solicitante', 
                                  'No. Comprovante',
                                 'Nº Centro de Custo', 
                                 'ID Despesa', 'Natureza']
        
        # Nao vou fazer calculos com esses dados
        df[colunas_para_converter] = df[colunas_para_converter].astype(str)

        return df

    # Define o periodo da analise
    def filter_by_date(self, df, date_column, start_date, end_date):
        # Convertendo a coluna "Data da Despesa" para datetime
        df[date_column] = pd.to_datetime(df[date_column])

        # Filtrando o DataFrame para obter somente as datas desejadas
        df = df[(df[date_column] >= start_date) & (df[date_column] <= end_date)]
        
        return df
    
    def ajustar_colunas_datas(self, df):
        """
        Ajusta automaticamente a largura das colunas que contêm datas.
        """
        for coluna in df.columns:
            if pd.api.types.is_datetime64_any_dtype(df[coluna]):
                df[coluna] = df[coluna].dt.strftime('%Y-%m-%d %H:%M:%S')

        print("Colunas com datas ajustadas automaticamente!")
    
    # Converte o DataFrame para um arquivo JSON e salva na pasta relatorio_flash.
    def salvar_df_como_json(self, df, nome_arquivo):
        # Converta o DataFrame para um dicionário
        df_dict = df.to_dict()

        # Encontre o caminho completo para a pasta relatorio_flash
        caminho_relatorio = self.caminho_utilizado

        # Crie a pasta se ela não existir
        if not os.path.exists(caminho_relatorio):
            os.makedirs(caminho_relatorio)

        # Salve o dicionário como um arquivo JSON
        with open(os.path.join(caminho_relatorio, nome_arquivo), 'w') as arquivo_json:
            json.dump(df_dict, arquivo_json)

        print(f"Arquivo JSON '{nome_arquivo}' salvo com sucesso na pasta relatorio_flash!")