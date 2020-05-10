import numpy as np
import pandas as pd
import xlrd
import openpyxl
tmp=pd.ExcelFile("imiona.xlsx")
df=pd.read_excel(tmp)

#print(df[df['Liczba']>1000])

#print(df[df['Imie']=='MICHAŁ'])

#print(df.agg({'Liczba':['sum']}))

#print(df[df['Rok']<2006].agg({'Liczba':['sum']}))

#print(df.groupby(['Plec']).agg({'Liczba':['sum']}))

#print(df.sort_values('Liczba', ascending=False).groupby(['Rok','Plec']).nth(0))

grouped=df.groupby(['Plec','Imie'])["Liczba"].sum().reset_index()
print(grouped.sort_values('Liczba', ascending=False).iloc[0:2])

