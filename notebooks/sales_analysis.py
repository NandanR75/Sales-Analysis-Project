
import pandas as pd

df = pd.read_csv('data/sales_data.csv')

print('Head of data:')
print(df.head())

print('\nBasic Info:')
print(df.info())

print('\nTotal Sales:', df['Sales'].sum())
print('Average Profit:', df['Profit'].mean())

print('\nSales by Region:')
print(df.groupby('Region')['Sales'].sum())
