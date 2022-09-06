import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression
from src.cria_data_frame import CriaDataFrame
from yellowbrick.regressor import ResidualsPlot


class MinimosQuadradosVelxVelMed(LinearRegression):
    """
    Método dos mínimos quadrados considerando relação velocidade media - velocidade na direção x
    """

    def __init__(self) -> None:
        self.data_frame = CriaDataFrame()
        self.numerador = 0
        self.denominador = 0
        self.lista_velx = None
        self.lista_vmed = None
        self.file_path = None
        self.mmq_velx_vmed = None

    def configura_var_independente_velx(self, file_path) -> list:
        """
        Retorna matriz da variavel independente velocidade da direção x.
        :param - file_path = string com caminho e nome do arquivo.
        :return - matriz numpy
        """
        self.file_path = file_path
        self.df = self.data_frame.cria_data_frame(self.file_path)
        self.lista_velx = np.array(self.df.velocity_x)
        self.mtx_velx = self.lista_velx.reshape(-1, 1)

        return self.mtx_velx

    def configura_var_dependente_vmed(self, file_path) -> list:
        """
        Retorna um matriz numpy da variavel dependente area
        :param - file_path = string com o caminho e nome do arquivo.
        :return - Matriz numpy
        """
        self.file_path = file_path
        self.df = self.data_frame.cria_data_frame(file_path)
        self.lista_vmed = np.array(self.df.mean_velocity)
        self.mtx_vmed = self.lista_vmed.reshape(-1, 1)

        return self.mtx_vmed

    def minimos_quadrados_velx_velmed(self, mtx_velx, mtx_vmed) -> None:
        """
        Executa o ajuste da reta pelo método dos mínimos quadrados.
        :param - mtx_velx = matriz numpy com os valores de velocidade na direção x.
               - mtx_vmed = matriz numpy com os valores de area.
        :return - None
        """
        self.mtx_velx = mtx_velx
        self.mtx_vmed = mtx_vmed
        self.mmq_velx_vmed = LinearRegression()
        self.mmq_velx_vmed.fit(mtx_velx, mtx_vmed)
        return None

    def obter_coef_linear(self) -> float:
        """
        Retorna o coeficiente linear da reta
        :param - None
        :return - float
        """
        self.coef_linear = self.mmq_velx_vmed.intercept_
        return float(round(self.coef_linear[0], 3))

    def obter_coef_angular(self) -> float:
        """
        Retorna o coeficiente angular da reta
        :param - None
        :return - float
        """
        self.coef_angular = self.mmq_velx_vmed.coef_
        return float(round(self.coef_angular[0][0], 3))

    def obter_variaveis_estimadas_de_vmed(self, var_independente) -> list:
        """
        Realiza as previsões de acordo com a reta ajustada
        :param = var_independente = lista de variaveis velocidades na direção x
        :return - list
        """
        self.var_independente_velx = var_independente
        self.var_estimada = self.mmq_velx_vmed.predict(self.var_independente_velx)
        return self.var_estimada

    def plotar_grafico_do_ajuste_velx_vmed(self, eixo_x, eixo_y, estimados) -> None:
        """
        Plota o gráfico do ajuste linear pelo mínimos quadrados.

        :param - eixo_x = variavel independente
               - eixo_y = variavel dependente
               - estimados = variaveis estimadas através do ajuste da reta pelo minimos quadrados
        :return - None
        """
        self.eixo_x = eixo_x
        self.eixo_y = eixo_y
        self.coef_cor = self.mmq_velx_vmed.score(self.eixo_x, self.eixo_y)
        self.eixo_x = eixo_x.ravel()
        self.eixo_y = eixo_y.ravel()
        self.estimados = estimados.ravel()

        self.grafico = px.scatter(
            x=self.eixo_x,
            y=self.eixo_y,
            title=f"Velocidade média(m/s) = {round(self.coef_angular[0][0],3)} * velocidade_x(m/s) + {round(self.coef_linear[0],3)} R² = {round(self.coef_cor, 3)} ",
        )
        self.grafico.add_scatter(
            x=self.eixo_x,
            y=self.estimados,
            name="Reta Ajustada",
        )
        self.grafico.update_layout(
            xaxis_title="Velocidade na direção x (m/s)",
            yaxis_title="Velocidade média da seção (m/s)",
        )
        self.grafico.show()

    def plotar_grafico_residuais_velx_vmed(self, eixo_x, eixo_y) -> None:
        """
        Plota o gráfico de visualização residual da relação entre os dados e a reta ajustada.
        :param - eixo_x = variavel independente
               - eixo_y = variavel dependente
        :return - None
        """
        self.eixo_x = eixo_x
        self.eixo_y = eixo_y

        self.visualizador = ResidualsPlot(self.mmq_velx_vmed)
        self.visualizador.fit(self.eixo_x, self.eixo_y)
        self.visualizador.poof()
