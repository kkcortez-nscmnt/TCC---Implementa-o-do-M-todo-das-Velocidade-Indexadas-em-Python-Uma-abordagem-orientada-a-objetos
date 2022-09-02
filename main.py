from src.mmq_level_area import MinimosQuadradosLevelArea

file_path = 'file.xlsx'

mmq_level_area = MinimosQuadradosLevelArea()
mmq_level_area.configura_var_independente_level(file_path)
mmq_level_area.configura_var_dependente_area(file_path)
lista_coeficientes = mmq_level_area.minimos_quadrados_level_area()
print(lista_coeficientes)
mmq_level_area.plota_grafico()
