import streamlit as st
from dataset import df
from utils import convert_csv, mensagem_sucesso

st.title('Dataset de Vendas')

#expender streamlit
#apresentando as colunas do dataset e permitindo que o usuário selecione quais colunas deseja visualizar
with st.expander('Colunas'):
    colunas = st.multiselect('Selecione as Colunas',
                             list(df.columns),
                             list(df.columns)
                             )
#Selecionando os dados unicos de categoria do produto e permitindo que o 
#usuário selecione quais categorias deseja visualizar
st.sidebar.title('Filtros')
with st.sidebar.expander('Categoria do Produto'):
    categorias = st.multiselect('Selecione as categorias',
                               list(df['Categoria do Produto'].unique()),
                               list(df['Categoria do Produto'].unique())
                               )
#selecionar em uma linha o preço do produto, com um slider que vai de 0 a 5000, 
#e que permite selecionar um intervalo de preço
with st.sidebar.expander('Preço do Produto'):
    preco = st.slider('Selecione o Preço',
                      0, 5000,
                      (0, 5000)
                     )
#Selecionando data da compra em um intervalo
#Atenção para o formato de tupla, que deve ser inserido antes dos chaves.
with st.sidebar.expander('Data da Compra'):
    data_compra = st.date_input('Selecione a data',
                      (df['Data da Compra'].min(),
                      df['Data da Compra'].max())
                     )

#apontando os filtros para o dataframe, utilizando a função query do pandas,
# que permite filtrar os dados de acordo com as condições especificadas
query = '''
    `Categoria do Produto` in @categorias and \
    @preco[0] <= Preço <= @preco[1] and \
    @data_compra[0] <= `Data da Compra` <= @data_compra[1]
'''

#assim vamos filtrar os dados do dataframe de acordo com os filtros selecionados pelo usuário
filtro_dados = df.query(query)
filtro_dados = filtro_dados[colunas]

st.dataframe(filtro_dados)

#mostrar em cada alteração do filtro, a quantidade de linhas e colunas do dataframe filtrado
st.markdown(f'A tabela possui :blue[{filtro_dados.shape[0]}] linhas e :blue[{filtro_dados.shape[1]}] colunas')

st.markdown('Escreva o nome do arquivo')

coluna1, coluna2 = st.columns(2)

with coluna1:
    nome_arquivo = st.text_input('', label_visibility='collapsed')
    nome_arquivo += '.csv'

with coluna2:
    st.download_button(
    'Baixar Arquivo',
    data=convert_csv(filtro_dados),
    file_name=nome_arquivo, 
    mime='text/csv',
    on_click=mensagem_sucesso
    )
    