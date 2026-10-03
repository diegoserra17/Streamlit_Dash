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
st.sidebar.title('Filtros')
with st.sidebar.expander('Categoria do Produto'):
    categoria = st.multiselect('Selecione as categorias',
                               list(df['Categoria do Produto'].unique()),
                               list(df['Categoria do Produto'].unique())
                               )
st.dataframe(df)