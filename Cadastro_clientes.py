import streamlit as st
import pandas as pd
from datetime import datetime
from datetime import date


st.set_page_config(
    page_title="Cadastro de clientes",
    page_icon="📔"
)


def funcao_cadastrar(nome, dt_nascimento, tipo):
    if nome and dt_nascimento<=date.today():
        st.session_state["sucesso"] = True
        nova_data = dt_nascimento.strftime('%d/%m/%Y')
        data1 = date.today()
        data_hoje = data1.strftime('%d/%m/%Y')
        with open ("Banco_de_dados.csv", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{nome},{nova_data},{data_hoje},{tipo}\n")
    else:
        st.session_state["sucesso"] = False


st.title("Cadastro de clientes")
st.divider()


nome = st.text_input("Digite o nome do cliente", key="nome")
dt_nascimento = st.date_input("Digite a data de nascimento", 
                   format="DD/MM/YYYY", 
                   key="data")
tipo = st.selectbox("Informe a natureza da pessoa",
                  ["Pessoa Física", "Pessoa Jurídica"],
                  key="Pessoa")
cadastrar = st.button("Cadastrar",
                      on_click=funcao_cadastrar,
                      args=[nome, dt_nascimento, tipo],
                      key="botao_cadastrar")


if cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cadastro realizado com sucesso.",
                   icon="✅")
    else:
        st.error("Houve algum problema no cadastro! Favor verificar Nome do cliente e Data de nascimento.",
                 icon="❌")


