import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from src.cria_data_frame import CriaDataFrame

plt.rcParams["figure.figsize"] = (12.0, 9.0)


class MinimosQuadradosLevelArea(LinearRegression):
    """
    Método dos mínimos quadrados considerando relação level-area
    """

    def __init__(self) -> None:
        self.data_frame = CriaDataFrame()
        self.numerador = 0
        self.denominador = 0
        self.lista_level = None
        self.lista_area = None
        self.file_path = None
        self.mmq_level_area = None

    def configura_var_independente_level(self, file_path) -> list:
        """
        Retorna matriz da variavel independente level.
        :param - file_path = string com caminho e nome do arquivo.
        :return - matriz numpay
        """
        self.file_path = file_path
        self.df = self.data_frame.cria_data_frame(self.file_path)
        self.lista_level = np.array(self.df.level)
        self.mtx_level = self.lista_level.reshape(-1, 1)

        return self.mtx_level

    def configura_var_dependente_area(self, file_path) -> list:
        """
        Retorna um matriz numpy da variavel independente area
        :param - file_path = string com o caminho e nome do arquivo.
        :return - Matriz numpy
        """
        self.file_path = file_path
        self.df = self.data_frame.cria_data_frame(file_path)
        self.lista_area = np.array(self.df.area)
        self.mtx_area = self.lista_area.reshape(-1, 1)

        return self.mtx_area

    def minimos_quadrados_level_area(self, mtx_level, mtx_area) -> None:
        """
        Executa o ajuste da reta pelo método dos mínimos quadrados.
        :param - mtx_level = matriz numpy com os valores de nível.
               - mtx_area = matriz numpy com os valores de area.
        :return - None
        """
        self.mtx_level = mtx_level
        self.mtx_area = mtx_area
        self.mmq_level_area = LinearRegression()
        self.mmq_level_area.fit(mtx_level, mtx_area)
        return None

    def obter_coef_linear(self) -> float:
        """
        Retorna o coeficiente linear da reta
        :param - None
        :return - float
        """
        self.coef_linear = self.mmq_level_area.intercept_
        return float(round(self.coef_linear[0], 3))

    def obter_coef_angular(self) -> float:
        """
        Retorna o coeficiente angular da reta
        :param - None
        :return - float
        """
        self.coef_angular = self.mmq_level_area.coef_
        return float(round(self.coef_angular[0][0], 3))

    def obter_variaveis_estimadas_de_area(self, var_independente) -> list:
        """
        Realiza as previsões de acordo com a reta ajustada
        """
        self.var_independente_level = var_independente
        self.var_estimada = self.mmq_level_area.predict(self.var_independente_level)
        return self.var_estimada
