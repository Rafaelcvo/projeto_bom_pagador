import streamlit as st
import pandas as pd
import numpy as np
# import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

st.title("Sistema Bom Pagador")
st.markdown("## Apresentação geral dos dados coletados.")

df = pd.read_csv("/home/rafael/git/projeto_bom_pagador/notebooks/paulo/base2.csv", index_col='Unnamed: 0')

transf = {0:"Aprovado", 1:"Reprovado"}
df['Situação'] = df['Situação'].map(transf)

st.dataframe(df)

# Campos de entrada de dados do cliente.

# Função transformar finalidade
def finalid(finalidade):
    if finalidade == "PERSONAL":
        return 1
    elif finalidade == "DEBTCONSOLIDATION":
        return 2
    elif finalidade == "EDUCATION":
        return 3
    elif finalidade == "HOMEIMPROVEMENT":
        return 4 
    elif finalidade == "MEDICAL":
        return 5 
    elif finalidade == "VENTURE":
        return 6 
    else:
        return 7


df['Finalidade'] = df['Finalidade'].map(finalid)

st.sidebar.subheader("Dados do clientes a ser avaliado")

renda_anual = st.sidebar.number_input("Renda", value=0)
idade = st.sidebar.number_input("Idade", value=0)
empr = st.sidebar.number_input("Emprestimo",value=0)

finalidade = st.sidebar.selectbox("Finalidade", [ "Pessoal", "Consolidação Debito", "Educação", "Melhoria em Casa", "Saúde", "Risco",])
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
else:
    finalidade = 7

tempo_empr = st.sidebar.number_input("Tempo de Empresa", value=0)

taxa = st.sidebar.number_input("Taxa", value=0.)

renda_empr = st.sidebar.number_input("Renda Emprestimo", value=0.)

# Inserindo um botao na tela
btn_predict = st.sidebar.button("Realizar consulta")

#----------------- Classificação do cliente utilizando algoritmos ---------------------------------------#
x = df.drop(['Situação'], axis=1)
y = df['Situação']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

clf = GaussianNB()
# clf = RandomForestClassifier(max_depth=15, random_state=0)
clf.fit(x_train, y_train)
model_treinado = clf.predict(x_test)


# Realizar a consulta quando o botao for acionado
if btn_predict:
    result = clf.predict([[renda_anual, idade, empr, finalidade, tempo_empr, taxa, renda_empr]])
    sit = "Aprovado" if result[0] == 0 else "Reprovado"
    st.sidebar.write("O cliente foi ", sit)
    acc = round(accuracy_score(y_test, model_treinado)*100,2)
    st.sidebar.write("Accuracy do modelo é: ", acc)
