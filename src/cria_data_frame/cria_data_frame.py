import pandas as pd


class CriaDataFrame:
    """
    Classe responsável pela criação do data frame.
    """

    def __init__(self) -> None:
        self.data_frame = None
        self.nome_do_arquivo_xlsx = None

    def cria_data_frame(self, file_path):
        self.nome_do_arquivo_xlsx = file_path
        self.data_frame = pd.read_excel(self.nome_do_arquivo_xlsx)

        return self.data_frame