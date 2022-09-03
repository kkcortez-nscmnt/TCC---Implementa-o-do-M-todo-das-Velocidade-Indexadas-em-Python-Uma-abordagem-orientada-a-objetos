from src.mmq_level_area import MinimosQuadradosLevelArea

file_path = "file.xlsx"

mmq_level_area = MinimosQuadradosLevelArea()
mtx_var_independente_level = mmq_level_area.configura_var_independente_level(file_path)
mtx_var_dependente_area = mmq_level_area.configura_var_dependente_area(file_path)
mmq_level_area.minimos_quadrados_level_area(
    mtx_var_independente_level, mtx_var_dependente_area
)
coef_linear = mmq_level_area.obter_coef_linear()
coef_angular = mmq_level_area.obter_coef_angular()
print(coef_linear)
print(type(coef_linear))
print(coef_angular)
print(type(coef_angular))
variaveis_estimadas_de_area = mmq_level_area.obter_variaveis_estimadas_de_area(
    mtx_var_independente_level
)
print(variaveis_estimadas_de_area)
