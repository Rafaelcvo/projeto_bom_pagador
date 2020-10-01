import streamlit as st
import pandas as pd


st.title("Sistema Bom Pagador")
st.markdown("Sistema de avaliador de clientes.")
st.markdown("Clientes externos.")

# Importando dataset externo que esta armazendo no drive.
df_ext = pd.read_csv('/home/rafael/git/projeto_bom_pagador/dataset/banco_externo.csv')
st.dataframe(df_ext.head(10))

st.markdown("# Clientes interno")
df_inter = pd.read_csv("/home/rafael/git/projeto_bom_pagador/dataset/banco_interno.csv")
st.dataframe(df_inter.head(10))

# Unindo os datasets
df = df_ext + df_inter

x = df.drop('default', axis=1)
y = df['default']
