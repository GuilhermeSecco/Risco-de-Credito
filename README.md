# 💳 Modelo de risco de Crédito
  Este projeto tem como objetivo avaliar o risco de crédito e prever a probabilidade de fraude em empréstimos utilizando Machine Learning. Além disso, os resultados são apresentados em um dashboard interativo no Power BI, facilitando a análise de risco por parte de gestores e analistas financeiros.

## Dashboard Online
  [Acesse o Dashboard Interativo no Power BI](https://app.powerbi.com/groups/me/reports/6513b484-a3eb-44a6-aaa1-42ba68dc71f5/aee932d08b9bc93b5870?ctid=ba201131-9621-49ca-b50d-57d968b4ac35&experience=power-bi&bookmarkGuid=b05b7c5b-be2a-4897-8862-7938efef6bd1)

## 📂 Estrutura do Repositório
    ├── Connection.py # Configura a conexão com banco MySQL (oculto por segurança)
    ├── dados_coletados.csv # Base de dados utilizada no treinamento
    ├── novos_dados.csv # Novos empréstimos para previsão
    ├── gerar_modelo.py # Script para treinar o modelo de Random Forest
    ├── gerar_previsoes.py # Script para aplicar o modelo em novos dados
    ├── modelo_treinado_fraude.pk # Modelo salvo (Random Forest)
    ├── previsoes_fraude.xlsx # Saída com probabilidades de fraude
    ├── Dashboard.pbix # Dashboard interativo em Power BI
    ├── Dashboard.pdf # Versão em PDF do dashboard
    └── README.md # Documentação do projeto

##  ⚙️ Como funciona

### Importando o Dataset
  O script gerar_modelo.py carrega o dataset por meio da conexão entre python e sql
  Os dados armazenados no Connection.py são necessários para uma conexão ocorrer, nesse projeto eles estão vazios por segurança

### Treinamento do Modelo
  O script gerar_modelo.py treina um modelo de Random Forest com base no histórico de empréstimos, em seguida o modelo é salvo em modelo_treinado_fraude.pk.
### Previsão em Novos Dados

O script gerar_previsoes.py aplica o modelo treinado em novos_dados.csv. Após isso as previsões são exportadas para previsoes_fraude.xlsx, incluindo a probabilidade de fraude.

### Dashboard Interativo

<img width="962" height="550" alt="image" src="https://github.com/user-attachments/assets/44dfaa94-6cc2-463a-bf3d-a811450cf10f" />
<br>
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


## 📐 Métricas do Modelo
    Durante o treino:
    F1-score: 97.84%
    Matriz de Confusão: [12999   293]
                        [  285 13130]
    
    Utilizando novos dados:
    F1 score: 95.29%
    Matriz de Confusão: [11341   870]
                        [  154 10361]

## 🚀 Tecnologias Utilizadas

    Python (pandas, scikit-learn, numpy) para analise, tratamento e modelagem dos dados.

    MySQL para armazenamento dos dados

    Machine Learning: Random Forest Classifier para analise preditiva

    Power BI para visualização dos dados

    Excel/CSV para armazenamento de previsões e datasets

