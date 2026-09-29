import plotly.express as px
from utils import df_rec_estado

#Gráfico de mapa de estados com a receita
#Scatter_geo é um gráfico de dispersão geográfica, que permite plotar pontos em um mapa com 
#base em coordenadas geográficas (latitude e longitude).
grafico_map_estado = px.scatter_geo(
    df_rec_estado,
    lat = 'lat',
    lon = 'lon',
    scope = 'south america',
    size = 'Preço',
    template = 'seaborn',
    hover_name = 'Local da compra',
    hover_data = {'lat': False, 'lon': False},
    title = 'Receita por Estado'
)