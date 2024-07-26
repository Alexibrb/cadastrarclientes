import os
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
###################### MENU PRINCIPAL #####################################
'''menu_background_color = "#000000"  # Cor de fundo do menu
menu_selected_color = "#ff0000"  # Cor do item selecionado
menu_unselected_color = "#FFFFFF"  # Cor dos itens não selecionados
menu_hover_color = "#262730"  # Cor dos itens não selecionados
selecao = option_menu(
    menu_title = 'Bem-vindo ao sistema, Faça seu cadastro',
    options = ["Cadastrar Dados", 'Visualizar Dados', 'Apagar Dados'],
    icons = ['person-lines-fill', 'book', 'trash3'],
    menu_icon = "clipboard2-check-fill",
    default_index = 0, orientation = 'horizontal',
    styles = {
        "container": {"padding": "5!important", "background-color": menu_background_color},
        "icon": {"color": menu_unselected_color, "font-size": "20px"},
        "nav-link": {"font-size": "20px", "text-align": "center", "margin": "0px", "--hover-color": menu_hover_color},
        "nav-link-selected": {"background-color": menu_selected_color},
    })'''
st.markdown('## Bem-vindo ao sistema, Faça seu cadastro')
btn_cadastro = st.button('Cadastrar Dados')
btn_visualizar = st.button('Visualizar Dados')
btn_apagar = st.button('Apagar Dados')
if btn_cadastro:
    cadastrar()
elif btn_visualizar:
    visualisar()

elif btn_apagar :
    apagar()







