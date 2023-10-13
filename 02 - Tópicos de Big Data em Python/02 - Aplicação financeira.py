import pandas as pd
import yfinance as yf

PETR4 = yf.download('PETR4.SA', start = '2023-10-01', end = '2023-10-13', group_by = 'ticker')
PRIO3 = yf.download('PRIO3.SA', start = '2023-10-01', end = '2023-10-13', group_by = 'ticker')
MGLU3 = yf.download('MGLU3.SA', start = '2023-10-01', end = '2023-10-13', group_by = 'ticker')

print(PETR4.head())
print(PRIO3.head())
print(MGLU3.head())