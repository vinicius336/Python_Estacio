import pandas as pd
import yfinance as yf

df = PETRO4 = yf.download('PRIO3.SA', start = '2020-01-01', end = '2023-10-13', group_by = 'ticker')
MGLU3 = yf.download('MGLU3.SA', start = '2023-01-01', end = '2023-10-13', group_by = 'ticker')
'''
print('#' * 80)
print(PRIO3.tail()); print(PRIO3)
print('#' * 80)
print(MGLU3.head()); print(MGLU3)
print('#' * 80)
'''
import seaborn as sns
sns.set_theme(style="darkgrid")
sns.displot(df['Close'].dropna(),kde=True)

import plotly.offline as py
import plotly.graph_objs as go
dados = [go.Scatter(x=df.index, y=df['Close'])]
layout = go.Layout(title='Histórico dos Preços da Ação',
yaxis={'title':'Preços'}, xaxis={'title': 'Período'})
fig = go.Figure(data=dados, layout=layout)
print(py.iplot(fig))