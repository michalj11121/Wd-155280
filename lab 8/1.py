import numpy as np
import pandas as pd
import xlrd
import openpyxl
tmp=pd.ExcelFile("imiona.xlsx")
df=pd.read_excel(tmp)
print(df)