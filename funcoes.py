import streamlit as st
import time

def spinner():
    with st.spinner('Aguarde... carregando a página'):
        # Simule uma tarefa de longa duração
        time.sleep(1)
def titulo():
    st.success("# Paulo Eiji Viana \n  Engenheiro Civil - :blue[CREABA 37645/D] | Fone: :blue[(77) 98813-3951] \n\n Rua São Lucas, 323 - Bairro São Vicente - Condeúba-BA")
    st.write("---")

def update_content():
    st.success("Dados Cadastrados com sucesso.")

def estilos():
    st.markdown("""
        <style>
        .stButton > button {
            brow-widget stButton #262730; 
            background-color: #000000; 
            padding: 25px 25px;  
            text-align: center;
            display: inline-block;
            font-size: 16px;
            margin: 10px 10px;
            cursor: pointer;
            border: 1px solid;
            border-radius: 8px;
            width: 100%;
            color: white;
        }

        .stButton > button:hover {
            background-color: #262730;
            color: white;
            padding: 25px 25px;  
            text-align: center;
            display: inline-block;
            font-size: 16px;
            margin: 10px 10px;
            cursor: pointer;
            border: 1px solid;
            border-radius: 8px;
            width: 100%;
            color: white;
        }

        .st-emotion-cache-1zhiv0.e1f1d6gn0 {
            background-color:#000000;
            color: gray;
        }

        .st-emotion-cache-q49buc{
            font-size: 24px;
            color: white;
        }

        .stAlert{
            text-align: center;
            padding: 3px 3px;
            margin: 3px 3px;

        }
	#MainMenu {
		visibility: hidden;

	 }
  	
       

	

        </style>
        """, unsafe_allow_html=True)
