# 💳 Modelo de risco de Crédito
  Este projeto tem como objetivo avaliar o risco de crédito e prever a probabilidade de fraude em empréstimos utilizando Machine Learning. Além disso, os resultados são apresentados em um dashboard interativo no Power BI, facilitando a análise de risco por parte de gestores e analistas financeiros.

## 📂 Estrutura do Repositório
    ├── dados_coletados.csv       # Base de dados utilizada no treinamento
    ├── novos_dados.csv           # Novos empréstimos para previsão
    ├── gerar_modelo.py           # Script para treinar o modelo de Random Forest
    ├── gerar_previsoes.py        # Script para executar o modelo em novos dados
    ├── modelo_treinado_fraude.pk # Modelo treinado salvo
    ├── previsoes_fraude.xlsx     # Resultado das previsões em planilha
    ├── Dashboard.pbix            # Dashboard interativo em Power BI
    ├── Dashboard.pdf             # Versão em PDF do dashboard

##  ⚙️ Como funciona

### Treinamento do Modelo
  O script gerar_modelo.py treina um modelo de Random Forest com base no histórico de empréstimos, em seguida o modelo é salvo em modelo_treinado_fraude.pk.
### Previsão em Novos Dados

O script gerar_previsoes.py aplica o modelo treinado em novos_dados.csv. Após isso as previsões são exportadas para previsoes_fraude.xlsx, incluindo a probabilidade de fraude.

### Dashboard Interativo

O arquivo Dashboard.pbix (Power BI) apresenta indicadores como:

    Total emprestado, recebido e saldo devedor;
    
    Probabilidade de fraude por contrato;
    
    Distribuição por sexo, estado civil e região;
    
    Quantidade de parcelas/dias em atraso;

## 📊 Exemplo de Resultados

|Nº Contrato|Valor do Empréstimo|Prazo Restante|Probabilidade de Fraude|
|:---:|---:|:---:|---:|
|322057780715|R$ 11.000,00|25 meses|93%|
|322057795715|R$ 3.000,00|25 meses|97%|
|322057799715|R$ 35.000,00|100 meses|89%|

## 🚀 Tecnologias Utilizadas

    Python (pandas, scikit-learn, numpy)

    Machine Learning: Random Forest Classifier

    Power BI para visualização dos dados

    Excel/CSV para armazenamento de previsões e datasets

