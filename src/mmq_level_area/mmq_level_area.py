import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression
from src.cria_data_frame import CriaDataFrame


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

    def plotar_gráfico(self, eixo_x, eixo_y, estimados) -> None:
        """
        Plota o gráfico do ajuste linear pelo mínimos quadrados.

        :param - eixo_x = variavel independente
               - eixo_y = variavel dependente
               - estimados = variaveis estimadas através do ajuste da reta pelo minimos quadrados
        :return - None
        """
        self.eixo_x = eixo_x.ravel()
        self.eixo_y = eixo_y.ravel()
        self.estimados = estimados.ravel()

        self.grafico = px.scatter(
            x=self.eixo_x,
            y=self.eixo_y,
            title=f"Área(m²) = {round(self.coef_angular[0][0],3)} * nível(m) + {round(self.coef_linear[0],3)} ",
        )
        self.grafico.add_scatter(
            x=self.eixo_x,
            y=self.estimados,
            name="Reta Ajustada",
        )
        self.grafico.update_layout(xaxis_title="Nível (m)", yaxis_title="Área (m²)")
        self.grafico.show()
