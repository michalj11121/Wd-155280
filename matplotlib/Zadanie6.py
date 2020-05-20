import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df= pd.read_excel(pd.ExcelFile("imiona.xlsx"),"Arkusz1")

wy1=p=df.groupby(['Plec']).agg({"Liczba":["sum"]})

wy3=p=df.groupby(['Rok']).agg({"Liczba":["sum"]})
m=df[df["Plec"]=='M'].groupby(['Rok']).sum()
k=df[df["Plec"]=='K'].groupby(['Rok']).sum()
plt.subplot(1, 3, 1)
plt.bar(['K','M'],[wy1.values[0][0],wy1.values[1][0]],color=['green','red'])
plt.ylabel('ilosc urodzen w (mln)')
plt.xlabel('plec')

plt.subplot(1,3,2)
plt.plot(df.Rok.unique(),[m.values[y][0] for y in range(len(m.values))],"r", label="M")
plt.plot(df.Rok.unique(),[k.values[y][0] for y in range(len(k.values))],"g", label="K")
plt.xticks(df.Rok.unique(), rotation=60)
plt.ylabel('ilosc urodzen w (mln)')
plt.xlabel('rok')
plt.legend()
plt.subplot(1,3,3)
plt.bar(df.Rok.unique(),[wy3.values[y][0] for y in range(len(wy3.values))],color="orange")
plt.xticks(df.Rok.unique(), rotation=60)
plt.ylabel('ilosc urodzen')
plt.xlabel('rok')
plt.show()