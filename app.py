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
cadastro = 'inativo'

st.markdown("""<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 5px;
		
    }

	.stTabs [data-baseweb="tab"] {
		height: 50px;
		width:200px;
        white-space: pre-wrap;
		background-color: #2e5db7; 
		border-radius: 15px 15px 0px 0px;
		gap: 5px;
		padding-top: 5px;
		padding-bottom: 5px;
    }

	.stTabs [aria-selected="true"] {
  		background-color:black;
  		
  	
	}

</style>""", unsafe_allow_html=True)

st.markdown('## Bem-vindo ao sistema\n ### Faça seu cadastro')

tab1, tab2, tab3 = st.tabs(["   Cadastrar Dados   ", "Visualizar Dados", "Apagar Dados"])
with tab1:
    cadastrar()
with tab2:
    visualisar()
with tab3:
    apagar()
























