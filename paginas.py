import streamlit as st
import pandas as pd
import os
from time import sleep


def are_fields_filled(nome, telefone, rg, cpf, endereco_obra, endereco_resid):
    return nome and telefone and rg and cpf and endereco_obra and endereco_resid


def visualisar():
    st.markdown("### 📢 :green[VISUALIZAR DADOS DO PROJETO]")
    st.write(":blue[Somente Administradores podem ver os dados]")
    if os.path.exists('clientes.csv'):
        tabclientes = pd.read_csv('clientes.csv', sep=",")
        senha = st.text_input("Digite a senha para visualizar os dados", type="password")
        btn_visualizar = st.button("Visualizar")
        if btn_visualizar:
            if senha == "ki47trqwe":

                st.table(tabclientes)

            else:
                st.error("Senha errada")
    else:
        st.warning("### Nenhum Registro Encontrado")


def apagar():
    st.markdown("### 📢 :red[APAGAR DADOS DO PROJETO]")
    st.write(":blue[Somente Administradores podem apagar os dados]")
    if os.path.exists('clientes.csv'):
        senha2 = st.text_input("Digite a Senha para Apagar os dados", type="password")
        btn_apagar = st.button("Apagar Dados dos Clientes", type="primary")
        if btn_apagar:
            if senha2 == "ki47trqwe":

                os.remove('clientes.csv')
                st.success("### Dados Deletados com sucesso")
                #sleep(1)
                #st.experimental_rerun()
            else:
                st.error("Senha errada")

    else:
        st.warning("### Nenhum Registro Encontrado")






