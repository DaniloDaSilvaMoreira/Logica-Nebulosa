### Logica-Nebulosa

### DESCRIÇÃO DO PROJETO

Este projeto implementa um Sistema de Análise de Risco de Crédito para um banco, utilizando Lógica Nebulosa (LogicA Fuzzy) por meio da biblioteca Scikit-Fuzzy. O sistema foi desenvolvido com base em uma entrevista com o Gerente de Análise de Risco da agência, que destacou as principais variáveis e regras usadas para avaliar o risco de crédito dos clientes. O objetivo é criar um sistema que possa avaliar o risco com base em variáveis financeiras chave, como histórico de crédito, renda mensal e dívida atual.

### PROPÓSITO

O sistema tem como proposito aprimorar a precisão e a consistência na avaliação de risco de crédito, auxiliando o banco a tomar decisões mais bem informadas ao conceder empréstimos ou crédito aos clientes. O sistema permite que o banco analise cada caso com base em critérios estabelecidos, oferecendo uma avaliação mais detalhada e precisa do nível de risco associado a cada cliente.

### INSTALAÇÃO E EXECUÇÃO DO CODIGO

### DESCRIÇÃO DAS VARIAVEIS DE ENTRADA (INPUTS)
- Histórico de Crédito:
  .Excelente: Clientes com excelente histórico de pagamento, sem registros de inadimplência.
  .Bom: Clientes com histórico positivo, com poucos ou nenhum atraso nos pagamentos.
  .Regular: Clientes com algum histórico de inadimplência, mas que ainda possuem um score razoável.
  .Ruim: Clientes com histórico ruim de pagamentos, com inadimplências frequentes.

- Renda Mensal:
  . Alta: Renda significativamente acima da média dos clientes.
  . Média: Renda que está na faixa média em comparação com outros clientes.
  . Baixa: Renda abaixo da média.

- Dívida Atual:
  . Baixa: Dívida que é baixa em relação à renda mensal.
  . Moderada: Dívida moderada em relação à renda mensal.
  . Alta: Dívida alta em relação à renda mensal.

### REGRAS FUZZY
Regra 1: Se o histórico de crédito é Excelente e a dívida atual é Baixa, então o risco é Baixo.
Regra 2: Se o histórico de crédito é Ruim e a dívida atual é Alta, então o risco é Alto.
Regra 3: Se o histórico de crédito é Bom, a renda mensal é Média, e a dívida atual é Moderada, então o risco é Médio.
Regra 4: Se o histórico de crédito é Bom e a renda mensal é Alta e a dívida atual é Moderada, então o risco de crédito é Médio.
Regra 5: Se o histórico de crédito é Regular e a renda mensal é Média e a dívida atual é Alta, então o risco de crédito é Alto.
