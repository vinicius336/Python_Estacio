import pandas as pd
import yfinance as yf

PRIO3 = yf.download('PRIO3.SA', start = '2023-01-01', end = '2023-10-13', group_by = 'ticker')
MGLU3 = yf.download('MGLU3.SA', start = '2023-01-01', end = '2023-10-13', group_by = 'ticker')

print('#' * 80)
print(PRIO3.tail())
print(PRIO3)
print('#' * 80)
print(MGLU3.head())
print(MGLU3)
print('#' * 80)