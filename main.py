from src.mmq_level_area import MinimosQuadradosLevelArea
from src.mmq_velmed_velx import MinimosQuadradosVelxVelMed
from src.obtem_serie_vazao import ObtemSerieVazao

file_path = "file.xlsx"

# AJUSTE DA RETA POR MÍNIMOS QUADRADOS RELAÇÃO NIVEL- AREA DA SEÇÃO DE CONTROLE

mmq_level_area = MinimosQuadradosLevelArea()
mtx_var_independente_level = mmq_level_area.configura_var_independente_level(file_path)

mtx_var_dependente_area = mmq_level_area.configura_var_dependente_area(file_path)
mmq_level_area.minimos_quadrados_level_area(
    mtx_var_independente_level, mtx_var_dependente_area
)
coef_linear = mmq_level_area.obter_coef_linear()
coef_angular = mmq_level_area.obter_coef_angular()
variaveis_estimadas_de_area = mmq_level_area.obter_variaveis_estimadas_de_area(
    mtx_var_independente_level
)
mmq_level_area.plotar_grafico_do_ajuste_level_area(
    mtx_var_independente_level, mtx_var_dependente_area, variaveis_estimadas_de_area
)
mmq_level_area.plotar_grafico_residuais_level_area(
    mtx_var_independente_level, mtx_var_dependente_area
)


# AJUSTE DA RETA POR MÍNIMOS QUADRADOS RELAÇÃO VEL_x - VEL_MED DA SEÇÃO DE CONTROLE

mmq_velx_vmed = MinimosQuadradosVelxVelMed()
mtx_var_independente_velx = mmq_velx_vmed.configura_var_independente_velx(file_path)
mtx_var_dependente_vmed = mmq_velx_vmed.configura_var_dependente_vmed(file_path)
mmq_velx_vmed.minimos_quadrados_velx_velmed(
    mtx_var_independente_velx, mtx_var_dependente_vmed
)
coef_linear = mmq_velx_vmed.obter_coef_linear()
coef_angular = mmq_velx_vmed.obter_coef_angular()
variaveis_estimadas_de_vmed = mmq_velx_vmed.obter_variaveis_estimadas_de_vmed(
    mtx_var_independente_velx
)

mmq_velx_vmed.plotar_grafico_do_ajuste_velx_vmed(
    mtx_var_independente_velx,
    mtx_var_dependente_vmed,
    variaveis_estimadas_de_vmed,
)
mmq_velx_vmed.plotar_grafico_residuais_velx_vmed(
    mtx_var_independente_velx, mtx_var_dependente_vmed
)


# OBTER SERIE DE VAZÃO

obter_serie_vazao = ObtemSerieVazao()
mtx_vazao_obs = obter_serie_vazao.configura_var_vazao_observada(file_path)
mtx_vazao_estimada = obter_serie_vazao.obter_serie_estimadas_de_vazao(
    variaveis_estimadas_de_vmed, variaveis_estimadas_de_area
)
obter_serie_vazao.obter_coeficiente_de_nash_sutcliffe(mtx_vazao_obs, mtx_vazao_estimada)
obter_serie_vazao.plotar_grafico_vazao_observada_vazao_estimada(
    file_path, mtx_vazao_obs, mtx_vazao_estimada
)
