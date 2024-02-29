from data_tools import DataTools
import pandas as pd

class DataProcessor:
    def __init__(self, download_path):
        self.download_path = download_path
        self.tools = DataTools(download_path)
