import numpy as np
import pandas as pd
import xlrd
import openpyxl
#1
import matplotlib.pyplot as plt
# tmp=pd.ExcelFile("imiona.xlsx")
# df=pd.read_excel(tmp)
# ts=df.groupby("Rok").agg({'Liczba':['sum']})

# ts.plot()
# plt.show()
#2
import matplotlib.pyplot as plt
# tmp=pd.ExcelFile("imiona.xlsx")
# df=pd.read_excel(tmp)
# grupa=df.agg({'Liczba':['sum']})
# wykres = grupa.plot.bar()
# wykres.set_ylabel('mld')
# wykres.set_xlabel('Urodzenia')
# wykres.legend()
# plt.title('Suma urodzeń w ciagu ostatnich 17 lat')
# plt.show()

#3
# tmp=pd.ExcelFile("imiona.xlsx")
# df=pd.read_excel(tmp)
# grupa=df[df["Rok"]>2011].groupby("Plec").agg({'Liczba':['sum']})

# wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
# plt.title('Suma zamównień dla sprzedawcy')
# plt.show()

#4


from sklearn import datasets


iris = datasets.load_iris()

df = pd.DataFrame(iris.data, columns = iris.feature_names)
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=iris.target)

plt.show()

#5
# df=pd.read_csv("zamowienia.csv",sep=";")
# ts=df.groupby(["Sprzedawca"]).agg({'idZamowienia':['count']})
# ts.plot()
# plt.show()