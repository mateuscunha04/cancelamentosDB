import pandas as pd

df = pd.read_csv('cancelamentos.csv')

print(df.info())
print(df.describe())

import plotly.express as px

fig = px.histogram(df, x='idade', color='cancelou', barmode='overlay', title="Distribuição dos clientes por idade")
fig.show()

fig = px.histogram(df, x='tempo_como_cliente', color='cancelou', barmode='overlay', title="Distribuição do tempo como clientes")
fig.show()

fig = px.histogram(df, x='total_gasto', color='cancelou', barmode='overlay', title="Distribuição dos gastos por clientes")
fig.show()

fig = px.histogram(df, x='dias_atraso', color='cancelou', barmode='overlay', title="Dias de atraso e cancelamentos")
fig.show()

fig = px.histogram(df, x='frequencia_uso', color='cancelou', barmode='overlay', title="Frequência de uso dos clientes")
fig.show()

fig = px.histogram(df, x='meses_ultima_interacao', color='cancelou', barmode='overlay', title="Últimas interações pelos clientes")
fig.show()

fig = px.histogram(df, x='ligacoes_callcenter', color='cancelou', title="Números de ligações ao Call Center")
fig.show()