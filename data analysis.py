import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
import seaborn as sns

#create a sample of 5000 invoices
def sample():
    retail = pd.read_excel("Online Retail.xlsx")
    retail = retail.head(5000)
    return retail


#removing null entries
def delete():
    retail = sample()
    retail = retail.dropna()
    retail = retail.drop_duplicates()
    return retail

#removing returns
def remove():
    retail = delete()
    retail_refurnished = retail[~retail["InvoiceNo"].str.contains("C", na = False)]
    return retail_refurnished

#creating revenue column
def specific():
    retail_revenue = remove()
    retail_revenue['Revenue'] = retail_revenue['Quantity'] * retail_revenue['UnitPrice']
    return retail_revenue

#plotting a revenue graph

retail_data = specific()
retail_table = retail_data[['Country', 'Revenue']]
retail_graph = sns.barplot(x = 'Country', y = 'Revenue', data = retail_table)
plt.title('Revenue vs Countries')
plt.show()

print(specific())
