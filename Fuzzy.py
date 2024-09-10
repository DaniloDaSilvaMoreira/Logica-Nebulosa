import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Variáveis de entrada
historico_credito = ctrl.Antecedent(np.arange(0, 11, 1), 'historico_credito')
renda_mensal = ctrl.Antecedent(np.arange(0, 11, 1), 'renda_mensal')
divida_atual = ctrl.Antecedent(np.arange(0, 11, 1), 'divida_atual')

# Variável de saída
risco = ctrl.Consequent(np.arange(0, 11, 1), 'risco')

# Funções de pertinência para o Histórico de Crédito
historico_credito['excelente'] = fuzz.trimf(historico_credito.universe, [7, 10, 10])
historico_credito['bom'] = fuzz.trimf(historico_credito.universe, [4, 7, 9])
historico_credito['regular'] = fuzz.trimf(historico_credito.universe, [2, 5, 8])
historico_credito['ruim'] = fuzz.trimf(historico_credito.universe, [0, 0, 4])

# Funções de pertinência para a Renda Mensal
renda_mensal['baixa'] = fuzz.trimf(renda_mensal.universe, [0, 0, 5])
renda_mensal['media'] = fuzz.trimf(renda_mensal.universe, [3, 5, 7])
renda_mensal['alta'] = fuzz.trimf(renda_mensal.universe, [5, 10, 10])

# Funções de pertinência para a Dívida Atual
divida_atual['baixa'] = fuzz.trimf(divida_atual.universe, [0, 0, 5])
divida_atual['moderada'] = fuzz.trimf(divida_atual.universe, [3, 5, 7])
divida_atual['alta'] = fuzz.trimf(divida_atual.universe, [5, 10, 10])

# Funções de pertinência para o Risco
risco['baixo'] = fuzz.trimf(risco.universe, [0, 0, 5])
risco['medio'] = fuzz.trimf(risco.universe, [3, 5, 7])
risco['alto'] = fuzz.trimf(risco.universe, [5, 10, 10])

# Regras fuzzy
regra1 = ctrl.Rule(historico_credito['excelente'] & divida_atual['baixa'], risco['baixo'])
regra2 = ctrl.Rule(historico_credito['ruim'] & divida_atual['alta'], risco['alto'])
regra3 = ctrl.Rule(historico_credito['bom'] & renda_mensal['media'] & divida_atual['moderada'], risco['medio'])
regra4 = ctrl.Rule(historico_credito['bom'] & renda_mensal['alta'] & divida_atual['moderada'], risco['medio'])
regra5 = ctrl.Rule(historico_credito['regular'] & renda_mensal['media'] & divida_atual['alta'], risco['alto'])

# Sistema de controle
sistema_controle_risco = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5])
simulacao_risco = ctrl.ControlSystemSimulation(sistema_controle_risco)

# Exemplo de uso: Configurando os valores de entrada
simulacao_risco.input['historico_credito'] = 8  # Excelente
simulacao_risco.input['renda_mensal'] = 6       # Média
simulacao_risco.input['divida_atual'] =  4      # Moderada

# Computando a saída
simulacao_risco.compute()

# Capturando o valor de saída
valor_risco = simulacao_risco.output['risco']

# Interpretando a classificação
if valor_risco <= 3:
    classificacao_risco = "Baixo"
elif 3 < valor_risco <= 7:
    classificacao_risco = "Médio"
else:
    classificacao_risco = "Alto"

# Resultado
print(f"Risco de crédito: {valor_risco:.2f} ({classificacao_risco})")
