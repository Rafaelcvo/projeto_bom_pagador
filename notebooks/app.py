import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

st.title("Sistema Bom Pagador")
st.markdown("Sistema de avalição de clientes.")
st.markdown("Clientes externos.")

# Importando dataset externo que esta armazendo no drive.
df_ext = pd.read_csv('/home/rafael/git/projeto_bom_pagador/dataset/banco_externo.csv', index_col="ID")
st.dataframe(df_ext)

st.markdown("Clientes interno")
df_inter = pd.read_csv("/home/rafael/git/projeto_bom_pagador/dataset/banco_interno.csv", index_col="ID")
st.dataframe(df_inter)

def get_data():
    return pd.read_csv("/home/rafael/git/projeto_bom_pagador/dataset/banco_original.csv")

# Função para treinar o modelo
def train_model():
    df = get_data()
    x = df.drop(['ID','Situacao'], axis=1)
    y = df['Situacao']
    clf = RandomForestClassifier(n_estimators=200, max_depth=7, max_features=3)
    clf.fit(x, y)
    return clf

# Treinando o modelo.
model = train_model()

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
    estado_civil = 1
elif estado_civil == "Solteiro":
    estado_civil = 2
else:
    estado_civil = 3


idade = st.sidebar.number_input("Idade", value=0)
tempo_empr =st.sidebar.number_input("Tempo de Empresa", value=0)

st.write(renda_anual, sexo, educa, estado_civil, idade, tempo_empr)
# Inserindo um botao na tela
btn_predict = st.sidebar.button("Realizar consluta")

# Realizar a consulta quando o botao for acionado
if btn_predict:
    result = model.predict([[renda_anual, sexo, educa, estado_civil, idade, tempo_empr]])
    sit = "Aprovado" if result[0] == 0 else "Reprovado"
    st.write("O cliente está ",sit)

