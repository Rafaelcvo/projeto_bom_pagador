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

# Convertendo variaveis 
transf = {0:"Aprovado", 1:"Reprovado"}

# Importando dataset externo que esta armazendo no drive.
st.markdown("Base de dados de clientes externos.")
# Linux
df_ext = pd.read_csv('/home/rafael/git/projeto_bom_pagador/dataset/banco_externo.csv', index_col="ID")

# Windows
# df_ext = pd.read_csv('C:/Users/Rafael/git/projeto_bom_pagador/dataset/banco_externo.csv', index_col="ID")

ext = df_ext.copy()
ext['Situacao'] = ext['Situacao'].map(transf)
st.dataframe(ext.head(5))

st.markdown("Base de dados de clientes interno.")

# Linux
df_inter = pd.read_csv("/home/rafael/git/projeto_bom_pagador/dataset/banco_interno.csv", index_col="ID")

# Windows
# df_inter = pd.read_csv("C:/Users/Rafael/git/projeto_bom_pagador/dataset/banco_interno.csv", index_col="ID")

inter = df_inter.copy()
inter['Situacao'] = inter['Situacao'].map(transf)
st.dataframe(inter.head(5))

# Linux
df =  pd.read_csv("/home/rafael/git/projeto_bom_pagador/dataset/banco_original.csv")
# Windows
# df =  pd.read_csv("C:/Users/Rafael/git/projeto_bom_pagador/dataset/banco_original.csv")

# Campos de entrada de dados do cliente.
st.sidebar.subheader("Dados do clientes a ser avaliado")
renda_anual = st.sidebar.number_input("Renda Anual", value=0)

sexo = st.sidebar.selectbox("Sexo", ['Masculino', 'Feminino'])
sexo = 1 if sexo == "Masculino" else 2

educa = st.sidebar.selectbox("Educação", [ "Pós-Graduação", "Universitário", "Ensino Médio", "Outros"])
if educa == "Pós-Graduação":
    educa = 1
elif educa == "Universitário": 
    educa = 2 
elif educa == "Ensino Médio": 
    educa = 3 
else:
    educa = 4

estado_civil = st.sidebar.selectbox("Estado Civil", ['Casado', 'Solteiro', 'Outros'])
if estado_civil == "Casado":
    estado_civil = 0
elif estado_civil == "Solteiro":
    estado_civil = 1
else:
    estado_civil = 2

idade = st.sidebar.number_input("Idade", value=0)
tempo_empr =st.sidebar.number_input("Tempo de Empresa", value=0)

# st.write(renda_anual, sexo, educa, estado_civil, idade, tempo_empr)

# Inserindo um botao na tela
btn_predict = st.sidebar.button("Realizar consulta")

#----------------- Classificação do cliente utilizando algoritmos ---------------------------------------#
x = df.drop(['ID','Situacao'], axis=1)
y = df['Situacao']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

clf = GaussianNB()
# clf = RandomForestClassifier(max_depth=15, random_state=0)
clf.fit(x_train, y_train)
model_treinado = clf.predict(x_test)

# Realizar a consulta quando o botao for acionado
if btn_predict:
    result = clf.predict([[renda_anual, sexo, educa, estado_civil, idade, tempo_empr]])
    sit = "Aprovado" if result[0] == 0 else "Reprovado"
    st.sidebar.write("O cliente foi ", sit)
    acc = round(accuracy_score(y_test, model_treinado)*100,2)
    st.sidebar.write("Accuracy do modelo é: ", acc)
