import streamlit as st
from dataset import df

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
    categoria = st.multiselect('Selecione as categorias',
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

st.dataframe(df)