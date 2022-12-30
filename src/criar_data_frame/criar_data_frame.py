import pandas as pd


class CriarDataFrame:
    """
    Classe responsável pela criação do data frame.
    """

    def __init__(self) -> None:
        self.data_frame = None
        self.nome_do_arquivo_xlsx = None

    def criar_data_frame(self, file_path):
        """
        Cria e retorna um data frame a partir de um arquivo excel.
        :para - file_path: string com o caminho/nome do arquivo.
        :return  - pandas data frame.
        """
        self.nome_do_arquivo_xlsx = file_path
        self.data_frame = pd.read_excel(self.nome_do_arquivo_xlsx)

        return self.data_frame
