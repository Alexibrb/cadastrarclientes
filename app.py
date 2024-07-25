import os
os.system('pip install -r requirements.txt')
from streamlit_option_menu import option_menu
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
menu_background_color = "#000000"  # Cor de fundo do menu
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
    })

if selecao == 'Cadastrar Dados':
    cadastrar()
elif selecao == 'Visualizar Dados':
    visualisar()

elif selecao == 'Apagar Dados':
    apagar()







