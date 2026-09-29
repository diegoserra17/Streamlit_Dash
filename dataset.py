import json
import pandas as pd

#Carregando o arquivo json
file = open('dados/vendas.json')
data = json.load(file)

#print(data)

#tranformando o json em um dataframe
df = pd.DataFrame.from_dict(data)

#print(df)

#Transformando a coluna 'Data da Compra' em datetime
df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

file.close()