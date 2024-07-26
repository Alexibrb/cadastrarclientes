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







