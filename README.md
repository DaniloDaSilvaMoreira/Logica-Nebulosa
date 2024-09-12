# LOGICA-NEBULOSA

# DESCRIÇÃO DO PROJETO - Sistema de Análise de Risco do Banco💵🏦

Este projeto implementa um Sistema de Análise de Risco de Crédito para um banco, utilizando Lógica Nebulosa (LogicA Fuzzy) por meio da biblioteca Scikit-Fuzzy. O sistema foi desenvolvido com base em uma entrevista com o Gerente de Análise de Risco da agência, que destacou as principais variáveis e regras usadas para avaliar o risco de crédito dos clientes. O objetivo é criar um sistema que possa avaliar o risco com base em variáveis financeiras chave, como histórico de crédito, renda mensal e dívida atual.

## PROPÓSITO🎯

O sistema tem como proposito aprimorar a precisão e a consistência na avaliação de risco de crédito, auxiliando o banco a tomar decisões mais bem informadas ao conceder empréstimos ou crédito aos clientes. O sistema permite que o banco analise cada caso com base em critérios estabelecidos, oferecendo uma avaliação mais detalhada e precisa do nível de risco associado a cada cliente.

## INSTALAÇÃO DO CODIGO/SISTEMA⚙️
1. Clone o repositório abaixo na sua máquina:
   git clone https://github.com/DaniloDaSilvaMoreira/Logica-Nebulosa.git.

2. Instale as dependências:
    pip install numpy scikit-fuzzy

## EXECUÇÃO DO CÓDIGO⚙️
1. Execute no terminal o comando "cd Logica-Nebulosa". Logo após, execute "code ."
2. Logo após abrirá uma IDE (visual Studio Code).
3.  Abra o arquivo "Fuzzy.py", onde deverá iniciar/rodar o codigo e inserir os dados solicitados (histórico de crédito, renda e dívida) para visualizar o resultado (Risco de crédito).

## COMO O SISTEMA FOI CONSTRUIDO, FUNCIONAMENTO E EXEMPLOS DE USO🛠️
1. O sistema de análise de risco de crédito foi construído utilizando lógica fuzzy (ou lógica nebulosa) para avaliar o risco de crédito de clientes. A lógica fuzzy permite modelar incertezas e imprecisões em situações onde a classificação tradicional (como "alta" ou "baixa") pode não ser suficiente. Isso é especialmente útil em cenários como a avaliação de crédito, onde as variáveis podem ter interpretações subjetivas. A construção do sistema foi com base em três variáveis principais: Histórico de Crédito, Renda Mensal e Dívida Atual; além da aplicação de regras fuzzy que são construídas com base em como as diferentes combinações das variáveis de entrada (inputs) que influenciam o risco.
2. O funcionamento do sistema funciona é a partir do momento que o usuário fornece valores numéricos para as variáveis historico_credito, renda_mensal, e divida_atual. Esses valores são mapeados para seus respectivos conjuntos fuzzy. Por exemplo, se hist_credito = 7.5, ele será parcialmente mapeado para os conjuntos fuzzy "Bom" e "Regular". O sistema aplica as regras fuzzy definidas para determinar os graus de risco associados a cada cenário do cliente. Portanto, o sistema combina os resultados das regras aplicadas e realiza a defuzzificação para calcular um valor de risco, que é a saída final do sistema.
3. Considere o cenário de exemplo: um cliente com histórico de Crédito: 7.5 (Parcialmente "Bom", parcialmente "Regular"), Renda Mensal: 5000 e Dívida Atual: 3000
Resultado: O sistema calculará o risco associado a esse cliente com base nas regras fuzzy que se aplicam a esses valores, geraando um risco de credito "baixo", com valor de 2.31 em uma escala de 0 a 10.

## DESCRIÇÃO DAS VARIAVEIS DE ENTRADA (INPUTS)▶️
- **Histórico de Crédito:**
  . Excelente: Clientes com excelente histórico de pagamento, sem registros de inadimplência.
  . Bom: Clientes com histórico positivo, com poucos ou nenhum atraso nos pagamentos.
  . Regular: Clientes com algum histórico de inadimplência, mas que ainda possuem um score razoável.
  . Ruim: Clientes com histórico ruim de pagamentos, com inadimplências frequentes.
- **Renda Mensal:**
  . Alta: Renda significativamente acima da média dos clientes.
  . Média: Renda que está na faixa média em comparação com outros clientes.
  . Baixa: Renda abaixo da média.
- **Dívida Atual:**
  . Baixa: Dívida que é baixa em relação à renda mensal.
  . Moderada: Dívida moderada em relação à renda mensal.
  . Alta: Dívida alta em relação à renda mensal.

## REGRAS FUZZY📊
- Se o histórico de crédito é Excelente e a dívida atual é Baixa, então o risco é Baixo.
- Se o histórico de crédito é Ruim e a dívida atual é Alta, então o risco é Alto.
- Se o histórico de crédito é Bom, a renda mensal é Média, e a dívida atual é Moderada, então o risco é Médio.

- Se o histórico de crédito é Bom e a renda mensal é Alta e a dívida atual é Moderada, então o risco de crédito é Médio.
- Se o historico de credito é excelente e a renda mensal é alta e divida atual é baixa, então o risco de crédito é baixo.
- Se o historico de credito é excelente e a renda mensal é média e a dívida atual é Moderada, então o risco de crédito é médio.
- Se o historico de credito é excelente e a renda mensal é baixa e a dívida atual é alta, então o risco de crédito é médio.
- Se o historico de credito é excelente e a renda mensal é baixa e a dívida atual é baixa, então o risco de crédito é baixo.
- Se o histórico de crédito é Bom e a renda mensal é Alta e a dívida atual é baixa, então o risco de crédito é baixo.
- Se o histórico de crédito é Bom e a renda mensal é media e a dívida atual é moderada, então o risco de crédito é medio.
- Se o histórico de crédito é Bom e a renda mensal é baixa e a dívida atual é alta, então o risco de crédito é alto.
- Se o histórico de crédito é Bom e a renda mensal é baixa e a dívida atual é baixa, então o risco de crédito é baixo.
- Se o histórico de crédito é Regular e a renda mensal é Média e a dívida atual é Alta, então o risco de crédito é Alto.
- Se o histórico de crédito é Regular e a renda mensal é alta e a dívida atual é baixa, então o risco de crédito é medio.
- Se o histórico de crédito é Regular e a renda mensal é Média e a dívida atual é moderada, então o risco de crédito é medio.
- Se o histórico de crédito é Regular e a renda mensal é baixa e a dívida atual é alta, então o risco de crédito é Alto.
- Se o histórico de crédito é Regular e a renda mensal é baixa e a dívida atual é baixa, então o risco de crédito é medio.
- Se o histórico de crédito é ruim e a renda mensal é alta e a dívida atual é baixa, então o risco de crédito é medio.
- Se o histórico de crédito é ruim e a renda mensal é media e a dívida atual é moderada, então o risco de crédito é alto.
- Se o histórico de crédito é ruim e a renda mensal é baixa e a dívida atual é alta, então o risco de crédito é alto.
- Se o histórico de crédito é ruim e a renda mensal é baixa e a dívida atual é baixa, então o risco de crédito é alto.

## OUTPUT✅💻
O sistema fornece como saída uma classificação do risco de crédito do cliente:
. Baixo: Baixo risco de inadimplência.
. Médio: Risco moderado, requerendo atenção.
. Alto: Alto risco de inadimplência, recomendando cautela na concessão de crédito.

## Tecnologias📲
. **Python 3.12.5**: Linguagem para o desenvolvimento.
. **NumPy**: Cálculos matemáticos precisos.
. **SciKit-Fuzzy**: Biblioteca para implementação da lógica fuzzy.
