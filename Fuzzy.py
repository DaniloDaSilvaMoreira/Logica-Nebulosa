import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Variáveis de entrada
historico_credito = ctrl.Antecedent(np.arange(0, 11, 1), 'historico_credito')
renda_mensal = ctrl.Antecedent(np.arange(0, 100001, 1000), 'renda_mensal')
divida_atual = ctrl.Antecedent(np.arange(0, 100001, 1000), 'divida_atual')

# Variável de saída
risco = ctrl.Consequent(np.arange(0, 11, 1), 'risco')

# Funções de pertinência para o Histórico de Crédito
historico_credito['excelente'] = fuzz.trimf(historico_credito.universe, [7, 10, 10])
historico_credito['bom'] = fuzz.trimf(historico_credito.universe, [4, 7, 9])
historico_credito['regular'] = fuzz.trimf(historico_credito.universe, [2, 5, 8])
historico_credito['ruim'] = fuzz.trimf(historico_credito.universe, [0, 0, 4])

# Funções de pertinência para a Renda Mensal
renda_mensal['baixa'] = fuzz.trimf(renda_mensal.universe, [0, 0, 25000])
renda_mensal['media'] = fuzz.trimf(renda_mensal.universe, [20000, 50000, 75000])
renda_mensal['alta'] = fuzz.trimf(renda_mensal.universe, [50000, 100000, 100000])

# Funções de pertinência para a Dívida Atual
divida_atual['baixa'] = fuzz.trimf(divida_atual.universe, [0, 0, 25000])
divida_atual['moderada'] = fuzz.trimf(divida_atual.universe, [20000, 50000, 75000])
divida_atual['alta'] = fuzz.trimf(divida_atual.universe, [50000, 100000, 100000])

# Funções de pertinência para o Risco
risco['baixo'] = fuzz.trimf(risco.universe, [0, 0, 5])
risco['medio'] = fuzz.trimf(risco.universe, [3, 5, 7])
risco['alto'] = fuzz.trimf(risco.universe, [5, 10, 10])

# Regras fuzzy
regras = [
    ctrl.Rule(historico_credito['excelente'] & renda_mensal['alta'] & divida_atual['baixa'], risco['baixo']),
    ctrl.Rule(historico_credito['excelente'] & renda_mensal['media'] & divida_atual['moderada'], risco['medio']),
    ctrl.Rule(historico_credito['excelente'] & renda_mensal['baixa'] & divida_atual['alta'], risco['medio']),
    ctrl.Rule(historico_credito['bom'] & renda_mensal['alta'] & divida_atual['baixa'], risco['baixo']),
    ctrl.Rule(historico_credito['bom'] & renda_mensal['media'] & divida_atual['moderada'], risco['medio']),
    ctrl.Rule(historico_credito['bom'] & renda_mensal['baixa'] & divida_atual['alta'], risco['alto']),
    ctrl.Rule(historico_credito['regular'] & renda_mensal['alta'] & divida_atual['baixa'], risco['medio']),
    ctrl.Rule(historico_credito['regular'] & renda_mensal['media'] & divida_atual['moderada'], risco['medio']),
    ctrl.Rule(historico_credito['regular'] & renda_mensal['baixa'] & divida_atual['alta'], risco['alto']),
    ctrl.Rule(historico_credito['ruim'] & renda_mensal['alta'] & divida_atual['baixa'], risco['medio']),
    ctrl.Rule(historico_credito['ruim'] & renda_mensal['media'] & divida_atual['moderada'], risco['alto']),
    ctrl.Rule(historico_credito['ruim'] & renda_mensal['baixa'] & divida_atual['alta'], risco['alto']),
    
    # Regras adicionais: histórico de crédito é maior que a renda e a dívida
    ctrl.Rule(historico_credito['excelente'] & renda_mensal['baixa'] & divida_atual['baixa'], risco['baixo']),
    ctrl.Rule(historico_credito['bom'] & renda_mensal['baixa'] & divida_atual['baixa'], risco['baixo']),
    ctrl.Rule(historico_credito['regular'] & renda_mensal['baixa'] & divida_atual['baixa'], risco['medio']),
    ctrl.Rule(historico_credito['ruim'] & renda_mensal['baixa'] & divida_atual['baixa'], risco['alto']),
]

# Sistema de controle
sistema_controle_risco = ctrl.ControlSystem(regras)
simulacao_risco = ctrl.ControlSystemSimulation(sistema_controle_risco)

# Apresentação inicial
print()
print("--------------- SISTEMA DE ANÁLISE DE RISCO DO BANCO -----------------")
print()

# Input com validação para números não negativos
while True:
    try:
        historico_credito_usuario = float(input("Digite o valor do Histórico de Crédito [0]Ruim a [10]Excelente: "))
        if 0 <= historico_credito_usuario <= 10:
            break
        else:
            print("Valor inválido! Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número entre 0 e 10.")

while True:
    try:
        renda_mensal_usuario = float(input("Digite o valor da Renda Mensal em reais [R$]: "))
        if renda_mensal_usuario >= 0:
            break
        else:
            print("Valor inválido! A renda mensal não pode ser negativa.")
    except ValueError:
        print("Por favor, digite uma renda R$ numérica positiva.")

while True:
    try:
        divida_atual_usuario = float(input("Digite o valor da Dívida Atual em reais [R$]: "))
        if divida_atual_usuario >= 0:
            break
        else:
            print("Valor inválido! A dívida atual não pode ser negativa.")
    except ValueError:
        print("Por favor, digite a divida R$ numérica positiva.")

# Configurando valores de entrada
simulacao_risco.input['historico_credito'] = historico_credito_usuario
simulacao_risco.input['renda_mensal'] = renda_mensal_usuario
simulacao_risco.input['divida_atual'] = divida_atual_usuario

# Computando a saída
simulacao_risco.compute()

# Capturando o valor de saída
valor_risco = simulacao_risco.output['risco']
porcentagem_risco = (valor_risco / 10) * 100

if valor_risco <= 3:
    classificacao_risco = "Baixo"
elif 3 < valor_risco <= 7:
    classificacao_risco = "Médio"
else:
    classificacao_risco = "Alto"

# Resultado
print(f"Risco de crédito: {porcentagem_risco:.2f}% ({classificacao_risco})")
print("-----------------------------------------------------------------------")
