import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

st.title("Sistema Bom Pagador")
st.markdown("## Apresentação geral dos dados coletados.")

df = pd.read_csv("base.csv", index_col='Unnamed: 0')

# Campos de entrada de dados do cliente.

st.sidebar.subheader("Dados do clientes a ser avaliado")

renda_anual = st.sidebar.number_input("Renda", value=0)
idade = st.sidebar.number_input("Idade", value=0)
empr = st.sidebar.number_input("Emprestimo",value=0)

finalidade = st.sidebar.selectbox("Finalidade", [ "Pessoal", "Consolidação Débito", "Educação", "Melhoria em Casa", "Saúde", "Risco",])
if finalidade == "Pessoal":
    finalidade = 1
elif finalidade == "Consolidação Debito": 
    finalidade = 2
elif finalidade == "Educação": 
    finalidade = 3 
elif finalidade == "Melhoria em Casa": 
    finalidade = 4 
elif finalidade == "Saúde": 
    finalidade = 5 
elif finalidade == "Risco": 
    finalidade = 6 

tempo_empr = st.sidebar.number_input("Tempo de Empresa", value=0)

taxa = st.sidebar.number_input("Taxa", value=0.)

# Inserindo um botao na tela
btn_predict = st.sidebar.button("Realizar consulta")

#----------------- Classificação do cliente utilizando algoritmos ---------------------------------------#
x = df.drop(['Situação'], axis=1)
y = df['Situação']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

clf = RandomForestClassifier(max_depth=15)
clf.fit(x_train, y_train)
model_treinado = clf.predict(x_test)


# Realizar a consulta quando o botao for acionado
if btn_predict:
    result = clf.predict([[renda_anual, idade, empr, finalidade, tempo_empr, taxa]])
    sit = "BOM" if result[0] == 0 else "MAU"
    acc = round(accuracy_score(y_test, model_treinado) * 100,2)
    resp = "O cliente tem {}% de ser um {} pagador!"
    st.sidebar.write(resp.format(acc, sit))
    nova = [renda_anual, idade, empr, finalidade, tempo_empr, taxa, result[0]]
    df.loc[len(df)] = nova
    df.to_csv("base.csv")
  
# Funcoes para conversoes.

def finalid(finalidade):
    if finalidade == 1:
        return "Pessoal"
    elif finalidade == 2:
        return "Consolidação Débito"
    elif finalidade == 3:
        return "Educação"
    elif finalidade == 4:
        return "Melhoria em Casa" 
    elif finalidade == 5:
        return "Saúde"
    elif finalidade == 6:
        return "Risco"

def situacao(situ):
    if situ == 0:
        return "Aprovado"
    elif situ == 1:
        return "Reprovado"

df['Finalidade'] = df['Finalidade'].map(finalid)
df["Situação"] = df['Situação'].map(situacao)
# Divisao da base.
df_int, df_ext = train_test_split(df, test_size=0.5)

st.markdown("### Base de dados interna")
st.dataframe(df_int)

st.markdown("### Base de dados externa")
st.dataframe(df_ext)

st.markdown("### Modelo sendo alimentado pelas consultas")
st.dataframe(df)