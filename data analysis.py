import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
import seaborn as sns
retail = pd.read_excel("Online Retail.xlsx")

#create a sample of 5000 invoices
retail = retail.head(5000)

#removing null entries
retail = retail.dropna()
retail = retail.drop_duplicates()

#removing returns
retail = retail[~retail["InvoiceNo"].str.contains("C", na=False)]

#creating revenue column
retail['Revenue'] = retail['Quantity'] * retail['UnitPrice']

#plotting a revenue graph
retail_data = retail[['Country', 'Revenue']]
retail_graph = sns.barplot(x = 'Country', y = 'Revenue', data = retail_data)
plt.title('Revenue vs Countries')
plt.show()

print(retail)
