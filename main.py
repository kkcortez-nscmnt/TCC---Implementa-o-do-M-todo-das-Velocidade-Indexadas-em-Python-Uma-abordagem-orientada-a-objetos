from src.mmq_nivel_area import MinimosQuadradosNivelArea
from src.mmq_velmed_velx import MinimosQuadradosVelxVelMed
from src.obtem_serie_vazao import ObtemSerieVazao

file_path = "file.xlsx"

# AJUSTE DA RETA POR MÍNIMOS QUADRADOS RELAÇÃO NIVEL- AREA DA SEÇÃO DE CONTROLE

mmq_nivel_area = MinimosQuadradosNivelArea()
mtx_var_independente_nivel = mmq_nivel_area.configura_var_independente_nivel(file_path)

mtx_var_dependente_area = mmq_nivel_area.configura_var_dependente_area(file_path)
mmq_nivel_area.minimos_quadrados_nivel_area(
    mtx_var_independente_nivel, mtx_var_dependente_area
)
coef_linear = mmq_nivel_area.obter_coef_linear()
coef_angular = mmq_nivel_area.obter_coef_angular()
variaveis_estimadas_de_area = mmq_nivel_area.obter_variaveis_estimadas_de_area(
    mtx_var_independente_nivel
)
mmq_nivel_area.plotar_grafico_do_ajuste_nivel_area(
    mtx_var_independente_nivel, mtx_var_dependente_area, variaveis_estimadas_de_area
)
mmq_nivel_area.plotar_grafico_residuais_nivel_area(
    mtx_var_independente_nivel, mtx_var_dependente_area
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
