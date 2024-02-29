import os

class DataTools:
    def __init__(self, path):
        self.path = path

    # Retorna o ultimo arquivo baixado
    def get_latest_file(self):
        # Lista todos os arquivos no diretório
        files = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]
        
        # Ordena os arquivos pela data de criação (mais recente primeiro)
        files.sort(key=lambda x: os.path.getmtime(os.path.join(self.path, x)), reverse=True)
        
        # Retorna o nome do arquivo mais recente
        return files[0] if files else None

    # outros metodos
    def graficos():
        pass