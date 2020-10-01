import streamlit as st
import pandas as pd


st.title("Sistema Bom Pagador")
st.markdown("Sistema de avalição de clientes.")
st.markdown("Clientes externos.")

# Importando dataset externo que esta armazendo no drive.
df_ext = pd.read_csv('/home/rafael/git/projeto_bom_pagador/dataset/banco_externo.csv')
st.dataframe(df_ext.head(5))

st.markdown("# Clientes interno")
df_inter = pd.read_csv("/home/rafael/git/projeto_bom_pagador/dataset/banco_interno.csv")
st.dataframe(df_inter.head(5))

# Unindo os datasets
df = df_ext + df_inter

x = df.drop('Situacao', axis=1)
y = df['Situacao']


# Campos de entrada de dados do cliente.
st.sidebar.subheader("Dados do clientes a ser avaliado")
renda_anual = st.sidebar.number_input("Renda Anual", value=0)
sexo = st.sidebar.selectbox("Sexo", ['Masculino', 'Feminino'])
educa = st.sidebar.selectbox("Educação", [ "Pós-Graduação", "Universitário", "Ensino Médio", "Outros"])
estado_civil = st.sidebar.selectbox("Estado Civil", ['Casado', 'Solteiro', 'Outros'])
idade = st.sidebar.number_input("Idade", value=0)
tempo_empr =st.sidebar.number_input("Tempo de Empresa", value=0)
