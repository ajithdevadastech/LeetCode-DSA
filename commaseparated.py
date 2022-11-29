#reads excel file column and make it comma separated

import pandas as pd

df = pd.ExcelFile('C:/Users/adevdas/Desktop/Tasks/Pricing Tool/TiC 500 Service Codes - Paid Claims Analysis - CY 2021.xlsx').parse('with description') #you could add index_col=0 if there's an index
x = df['SVCCOD']

i = 0
for x1 in x:
    x[i] = "'" + str(x1) + "',"
    i = i + 1

print(*x)

