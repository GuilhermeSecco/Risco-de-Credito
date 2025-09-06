#Criando a função de criação do modelo
def criacao_treinamento_modelo():
    #Importando os requisitos
    import pandas as pd
    import numpy as np
    import mysql.connector as sql
    import Connection

    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelEncoder, MinMaxScaler
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
    from imblearn import under_sampling, over_sampling
    from imblearn.over_sampling import SMOTE
    import joblib

    #Conectando com o servidor MySQL
    conexao = sql.CMySQLConnection(host='localhost',
                                   user=Connection.User(),
                                   password=Connection.Password(),
                                   database='risco_credito')

    #Carregando o dataset
    df_original = pd.read_sql('SELECT * FROM dados_coletados', conexao)

    #Trocando labels
    df_original['Estado_Civil'] = df_original['Estado_Civil'].replace(['NENHUM'], 'OUTRO')
    df_original['Estado_Civil'] = df_original['Estado_Civil'].replace(['UNIÃO ESTAVEL'], 'CASADO (A)')

    #Trocando idade por faixa etária
    bins = [0, 21, 30, 40, 50, 60, 100]
    labels = ['Até 21 Anos', 'De 22 até 30 Anos', 'De 31 até 40 Anos', 'De 41 até 50 Anos', 'De 51 até 60 Anos',
              'Acima de 60 Anos']
    df_original['Faixa_Etaria'] = pd.cut(df_original['Idade'], bins=bins, labels=labels)

    #Trocando valor de randa por faixa salarial
    bins = [-100, 1000, 2000, 3000, 5000, 10000, 20000, 30000, 9000000000]
    labels = ['Até 1k', 'De 1k até 2k', 'De 2k até 3k', 'De 3k até 5k', 'De 5k até 10k', 'De 10k até 20k',
              'de 20k até 30k', 'Acima de 30k']
    df_original['Faixa_Salarial'] = pd.cut(df_original['Valor_Renda'], bins=bins, labels=labels)

    #Trocando a quantidade de dias de atraso por Faixa de dias
    bins = [-100, 30, 60, 90, 180, 240, 360, 500]
    labels = ['Até 30 dias', 'De 31 até 60', 'De 61 até 90', 'De 91 até 180', 'De 181 até 240', 'De 241 até 360',
              'Acima de 360']
    df_original['Faixa_Dias_Atraso'] = pd.cut(df_original['QT_Dias_Atraso'], bins=bins, labels=labels)

    #Trocando por faixas de meses
    bins = [0, 60, 120, 200, 720]
    labels = ['Até 60 Meses', 'De 61 até 120 Meses', 'De 121 até 200 Meses', 'Acima de 200 Meses']
    df_original['Faixa_Prazo_Emprestimo'] = pd.cut(df_original['Prazo_Emprestimo'], bins=bins, labels=labels)

    #Trocando por faixas de meses
    bins = [-1, 60, 120, 200, 500]
    labels = ['Até 60 Meses', 'De 61 até 120 Meses', 'De 121 até 200 Meses', 'Acima de 200 Meses']
    df_original['Faixa_Prazo_Restante'] = pd.cut(df_original['Prazo_Restante'], bins=bins, labels=labels)

    #Separando as colunas que serão utilizadas pelo modelo
    columns = ['Sexo', 'UF_Cliente', 'Perc_Juros',
               'VL_Emprestimo', 'VL_Emprestimo_ComJuros', 'QT_Total_Parcelas_Pagas',
               'QT_Total_Parcelas_Pagas_EmDia', 'QT_Total_Parcelas_Pagas_EmAtraso',
               'Qt_Renegociacao', 'Estado_Civil', 'QT_Parcelas_Atraso', 'Saldo_Devedor',
               'Total_Pago', 'Faixa_Prazo_Restante', 'Faixa_Salarial', 'Faixa_Prazo_Emprestimo', 'Faixa_Etaria',
               'Faixa_Dias_Atraso', 'Possivel_Fraude']

    #Carregando os dados
    df_dados = pd.DataFrame(df_original, columns=columns)

    #Separando as variaveis categoricas
    variaveis_categoricas = []
    for i in df_dados.columns[0:18].tolist():
        if df_dados.dtypes[i] == 'object' or df_dados.dtypes[i] == 'category':
            variaveis_categoricas.append(i)

    #Usando o label encoder nas variáveis categóricas
    lb = LabelEncoder()
    for var in variaveis_categoricas:
        df_dados[var] = lb.fit_transform(df_dados[var])

    #Separando os valores que serão utilizados pelo modelo e o valor alvo
    PREDITORAS = df_dados.iloc[:, 0:18]
    TARGET = df_dados.iloc[:, 18]

    #Usando Smote para balancear os valores
    balanceador = SMOTE()
    PREDITORAS_RES, TARGET_RES = balanceador.fit_resample(PREDITORAS, TARGET)

    #Separando entre teste e treino
    X_train, X_test, y_train, y_test = train_test_split(PREDITORAS_RES, TARGET_RES, test_size=0.3, random_state=42)

    #Normalizando os valores
    Normalizador = MinMaxScaler()
    X_train_normalizado = Normalizador.fit_transform(X_train)
    X_test_normalizado = Normalizador.transform(X_test)

    #Random Forest
    clf = RandomForestClassifier(n_estimators=100, criterion='entropy', max_depth=3,
                                 min_samples_leaf=10, min_samples_split=2)

    #Criando e Treinando o Modelo
    print("Criando e treinando o modelo...")
    clf = clf.fit(X_train_normalizado, y_train)

    #Avaliando o modelo
    y_pred = clf.predict(X_test_normalizado)
    print("\nAvaliação do modelo:")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred, pos_label="Sim"))
    print("Recall:", recall_score(y_test, y_pred, pos_label="Sim"))
    print("F1-score:", f1_score(y_test, y_pred, pos_label="Sim"))
    print("\nMatriz de Confusão:\n", confusion_matrix(y_test, y_pred))
    print("\nRelatório de Classificação:\n", classification_report(y_test, y_pred))

    #Salvando o modelo
    joblib.dump(clf, 'modelo_treinado_fraude.pk')
    print("Modelo treinado e salvo com sucesso!")

def main():
    criacao_treinamento_modelo()

if __name__ == '__main__':
    main()

