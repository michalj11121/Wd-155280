import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df= pd.read_excel(pd.ExcelFile("imiona.xlsx"),"Arkusz1")

m=df[df["Plec"]=='M'].groupby(['Rok']).sum()
k=df[df["Plec"]=='K'].groupby(['Rok']).sum()
plt.bar(df.Rok.unique(),[m.values[y][0] for y in range(len(m.values))], label="M")
plt.bar(df.Rok.unique(),[k.values[y][0] for y in range(len(k.values))], label="K",bottom=[m.values[y][0] for y in range(len(m.values))])
plt.xticks(df.Rok.unique(), rotation=60)
plt.ylabel('ilosc urodzen w (mln)')
plt.xlabel('rok')
plt.legend(loc='best')
plt.show()