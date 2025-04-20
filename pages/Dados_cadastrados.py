import streamlit as st
import pandas as pd


st.title("Dados cadastrados")
st.divider()


dados = pd.read_csv("Banco_de_dados.csv")
st.dataframe(dados)