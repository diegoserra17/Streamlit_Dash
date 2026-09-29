import streamlit as st
import plotly.express as px
from dataset import df
from utils import format_number
from graficos import grafico_map_estado, grafico_rec_mensal, grafico_rec_estado

#Configurando a tela do streamlit para Wide (Grantindo que 
#o dashboard ocupe toda a tela) - Colocar sempre antes do Título
st.set_page_config(layout='wide')

#Titulo do Dashboard
st.title("Dashboard de Vendas: 🛒")

#Criando as abas do dashboard
aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])
with aba1:
    st.dataframe(df)
with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita Total', format_number(df['Preço'].sum(), 'R$'))
        #Incluindo o gráfico de mapa de estados com a receita
        st.plotly_chart(grafico_map_estado, use_container_width=True)
        st.plotly_chart(grafico_rec_estado, use_container_width=True)
    with coluna2:
        st.metric('Quantidade de Vendas', format_number(df.shape[0]))
        st.plotly_chart(grafico_rec_mensal, use_container_width=True)