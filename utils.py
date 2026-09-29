from dataset import df
import pandas as pd

#Função para formatar números grandes em milhares e milhões
def format_number(value, prefix = ''):
    for unit in ['', 'mil']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} milhões'

#Agrupando o dataframe por estado e somando a receita
df_rec_estado = df.groupby('Local da compra')[['Preço']].sum()

#Considerando que pode haver registros duplicados
#Passamos quais são os dados que vai estar trazendo.
#Ordenando o dataframe pelo valor da receita de forma decrescente
df_rec_estado = df.drop_duplicates(subset='Local da compra')[['Local da compra', 'lat','lon']].merge(df_rec_estado, left_on='Local da compra', right_index=True).sort_values('Preço', ascending=False)

#print(df_rec_estado)

# 2 - Dataframe Receita Mensal
#Aqui passamos a coluna 'Data da compra' para o index do dataframe, 
#para que possamos agrupar por mês e ano
df_rec_mensal = df.set_index('Data da Compra').groupby(pd.Grouper(freq='ME'))['Preço'].sum().reset_index()
#vamos inserir uma coluna com o mês e ano para facilitar a visualização
df_rec_mensal['Ano'] = df_rec_mensal['Data da Compra'].dt.year
df_rec_mensal['Mes'] = df_rec_mensal['Data da Compra'].dt.month_name()
#print(df_rec_mensal)

# 3 - Dataframe Receitas por Categoria
#ascendente, ou seja, do maior para o menor valor de receita
df_rec_categoria = df.groupby('Categoria do Produto')[['Preço']].sum().sort_values('Preço', ascending=False)
#print(df_rec_categoria.head())

# 4 - Dataframe Vendedores
df_vendedores = pd.DataFrame(df.groupby('Vendedor')['Preço'].agg(['sum', 'count']))
print(df_vendedores)
#print(df_vendedores)