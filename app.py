import streamlit as st
import pandas as pd
import os
from time import sleep
from funcoes import *
from paginas import *

########## CONFIGURAÇÕES
st.set_page_config(
    page_title="Cadastro de Clientes",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="auto"
)
estilos()
titulo()


st.markdown("""<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 3px;
		
    }

	.stTabs [data-baseweb="tab"] {
		height: 40px;
		width:200px;
        	white-space: pre-wrap;
		background-color: #2e5db7; 
		border-radius: 10px 10px 0px 0px;
		gap: 3px;
		padding-top: 5px;
		padding-bottom: 5px;
    }

	.stTabs [aria-selected="true"] {
  		background-color:#0c3181;
  		
  	
	}

</style>""", unsafe_allow_html=True)

st.markdown('## Bem-vindo ao sistema\n ### Faça seu cadastro')

tab1, tab2, tab3 = st.tabs(["   Cadastrar Dados   ", "Visualizar Dados", "Apagar Dados"])
with tab1:
    st.markdown("### 📢 :violet[CADASTRAR INFORMAÇÕES DO PROJETO]")
    st.write(":blue[Por favor, preencha todos os dados]")
    if os.path.exists('clientes.csv'):
        tabclientes = pd.read_csv('clientes.csv', sep=",")


        with st.form("configp", clear_on_submit=True):
            cidade = st.selectbox(label="Selecione a sua Cidade:", options=[
                "Clique aqui",
                "Condeúba",
                "Maetinga",
                "Pres. Jânio Quadros",
                "Cordeiros",
                "Piripá",
                "Mortugaba"
            ])
            nome = st.text_input("Digite seu nome", placeholder="Nome Completo")
            telefone = st.text_input("Digite seu Telefone", placeholder="(xx) xxxx-xxxx")
            rg = st.text_input("Digite seu RG", placeholder="xxxxxxxx-xx")
            cpf = st.text_input("Digite seu CPF", placeholder="xxx.xxx.xxx-xx")
            endereco_obra = st.text_input("Digite o Endereço da Obra", placeholder="Rua, nº e bairro")
            endereco_resid = st.text_input("Digite o Endereço Residencial", placeholder="Rua, nº e bairro")
            obs = st.text_area("Observação", placeholder="não obrigatório")
            # Mensagem de aviso
            warning_message = st.empty()

            # Desativando o botão se algum campo estiver vazio
            if not are_fields_filled(nome, telefone, rg, cpf, endereco_obra, endereco_resid):
                warning_message.warning("Por favor, preencha todos os campos.")
            else:
                warning_message.empty()

            btn_cadastro = st.form_submit_button("Cadastrar Dados")

            if btn_cadastro and are_fields_filled(nome, telefone, rg, cpf, endereco_obra, endereco_resid):
                cidadec = cidade
                cliente = nome
                fone = telefone
                rgc = rg
                cpfc = cpf
                end1 = endereco_obra
                end2 = endereco_resid
                obs1 = obs
                data2 = pd.DataFrame(tabclientes)
                d = {"Cidade": cidadec,
                     "Nome": cliente,
                     "Telefone": fone,
                     "RG": rgc,
                     "CPF": cpfc,
                     "Endereço_Obra": end1,
                     "Endereço_Residencial": end2,
                     "Observação": obs1
                     }
                df2 = pd.DataFrame(d, index=[0])
                data2 = pd.concat([data2, df2], ignore_index=True)
                data2.to_csv('clientes.csv', index=False)
                st.success("# Cadastro Efetuado com sucesso!!!!")

                st.table(data2.tail(1))
		    
	btn_confirmar = st.form_submit_button("Confirmar Dados")

	if btn_confirmar:   
		st.experimental_rerun()





    else:

        with st.form("config", clear_on_submit=True):
            cidade = st.selectbox(label="Selecione a sua Cidade:", options=[
                "Clique aqui",
                "Condeúba",
                "Maetinga",
                "Pres. Jânio Quadros",
                "Cordeiros",
                "Piripá",
                "Mortugaba"
            ])
            nome = st.text_input("Digite seu nome", placeholder="Nome Completo")
            telefone = st.text_input("Digite seu Telefone", placeholder="(xx) xxxx-xxxx")
            rg = st.text_input("Digite seu RG", placeholder="xxxxxxxx-xx")
            cpf = st.text_input("Digite seu CPF", placeholder="xxx.xxx.xxx-xx")
            endereco_obra = st.text_input("Digite o Endereço da Obra", placeholder="Rua, nº e bairro")
            endereco_resid = st.text_input("Digite o Endereço Residencial", placeholder="Rua, nº e bairro")
            obs = st.text_area("Observação", placeholder="não obrigatório")
            # Mensagem de aviso
            warning_message = st.empty()

            # Desativando o botão se algum campo estiver vazio
            if not are_fields_filled(nome, telefone, rg, cpf, endereco_obra, endereco_resid):
                warning_message.warning("Por favor, preencha todos os campos.")
            else:
                warning_message.empty()

            btn_cadastro = st.form_submit_button("Cadastrar Dados")

            if btn_cadastro and are_fields_filled(nome, telefone, rg, cpf, endereco_obra, endereco_resid):

                cidadec = cidade
                cliente = nome
                fone = telefone
                rgc = rg
                cpfc = cpf
                end1 = endereco_obra
                end2 = endereco_resid
                obs1 = obs

                data2 = pd.DataFrame(columns=['Cidade',
                                              'Nome',
                                              'Telefone',
                                              'RG',
                                              'CPF',
                                              'Endereço_Obra',
                                              'Endereço_Residencial',
                                              'Observação'
                                              ])
                d = {"Cidade": cidadec,
                     "Nome": cliente,
                     "Telefone": fone,
                     "RG": rgc,
                     "CPF": cpfc,
                     "Endereço_Obra": end1,
                     "Endereço_Residencial": end2,
                     "Observação": obs1
                     }

                df2 = pd.DataFrame(d, index=[0])
                data2 = pd.concat([data2, df2], ignore_index=True)
                data2.to_csv('clientes.csv', index=False)
                st.success("# Cadastro Efetuado com sucesso!!!!")
                
                st.table(data2.tail(1))
	btn_confirmar2 = st.form_submit_button("Confirmar Dados")

	if btn_confirmar2:   
		st.experimental_rerun()
with tab2:
    visualisar()
with tab3:
    apagar()
























