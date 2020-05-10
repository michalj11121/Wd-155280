import numpy as np
import pandas as pd
import xlrd
import openpyxl

df=pd.read_csv("zamowienia.csv",sep=";")
#print(df)

#print(df["Sprzedawca"].unique())

#print(df.nlargest(5,["Utarg"])["Utarg"])

#print(df.groupby(["Sprzedawca"]).agg({'idZamowienia':['count']}))

#print(df.groupby(["Kraj"]).agg({'idZamowienia':['count']}))

#print(df[((df["Kraj"]=="Polska") & (df["Data zamowienia"]> '2005-01-01'))].agg({'idZamowienia':['count']}))

print(df[((df["Data zamowienia"] < '2005-01-01') & (df["Data zamowienia"] >= '2004-01-01'))].agg({'Utarg':['mean']}))

#dane2004=df[((df["Data zamowienia"] < '2005-01-01') & (df["Data zamowienia"] >= '2004-01-01'))]
#dane2004.to_csv('zamówienia_2004.csv', header=None, index=False)
#dane2005=df[((df["Data zamowienia"] < '2006-01-01') & (df["Data zamowienia"] >= '2005-01-01'))]
#dane2005.to_csv('zamówienia_2005.csv', header=None, index=False)