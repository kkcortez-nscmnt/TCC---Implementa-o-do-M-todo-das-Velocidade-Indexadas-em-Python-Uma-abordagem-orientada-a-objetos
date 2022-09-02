import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12.0, 9.0)
from src.cria_data_frame import CriaDataFrame

class MinimosQuadradosLevelArea:
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

    def configura_var_independente_level(self, file_path) -> list:
        """
        Retorna lista da variavel independente Level
        :param - None
        :return - list
        """
        self.file_path = file_path
        self.df = self.data_frame.cria_data_frame(self.file_path)
        self.lista_level = self.df.level.tolist()
        
        return self.lista_level

    def configura_var_dependente_area(self, file_path) -> list:
        """
        Retorna lista da variavel independente Level
        :param - None
        :return - list
        """
        self.file_path = file_path
        self.df = self.data_frame.cria_data_frame(file_path)
        self.lista_area = self.df.area.tolist()
        
        return self.lista_area
    
    def minimos_quadrados_level_area(self) -> list:
        """
        Executa o método dos mínimos quadrados.
        :patam - None
        :return - list
        """

        self.x_var_independente_level = self.configura_var_independente_level(self.file_path)
        self.y_var_dependente_area = self.configura_var_dependente_area(self.file_path)
        self.x_media = np.mean(self.x_var_independente_level)
        self.y_media = np.mean(self.y_var_dependente_area)

        for i in range(len(self.x_var_independente_level)):
            self.numerador += (self.x_var_independente_level[i] - self.x_media)*(
                self.y_var_dependente_area[i] - self.y_media
            )

            self.denominador += (self.x_var_independente_level[i] - self.x_media) ** 2

            self.coef_ang = self.numerador / self.denominador
            self.coef_lin = self.y_media - self.coef_ang*self.x_media

            self.lista_coeficientes = [self.coef_ang,self.coef_lin]

            return self.lista_coeficientes
        
    def plota_grafico(self) -> None:
        """
        Plota gráfico 
        :param = none
        :return = none
        """
        self.y_pred = self.coef_ang*np.array(self.x_var_independente_level) + self.coef_lin
        plt.scatter(self.x_var_independente_level, self.y_var_dependente_area)
        plt.plot([min(self.x_var_independente_level), max(self.x_var_independente_level)], [min(self.y_pred), max(self.y_pred)], color='red')
        plt.title(f'Area = {round(self.coef_ang, 3)} * nivel + {round(self.coef_lin, 3)}')
        plt.show()

        return None



    