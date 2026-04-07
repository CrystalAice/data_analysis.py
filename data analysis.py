import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
import seaborn as sns

#create a sample of 5000 invoices
def sample():
    retail = pd.read_excel("Online Retail.xlsx")
    #Converting InvoiceDate to a proper datetime object
    retail["InvoiceDate"] = retail.to_datetime(retail["InvoiceDate"])
    return retail


#removing null entries
def delete():
    retail = sample()  
    retail = retail.dropna(subset=["Quantity", "UnitPrice", "Country"])
    retail = retail.drop_duplicates()
    return retail

#removing returns
def remove():
    retail = delete()
    retail_refurnished = retail[~retail["InvoiceNo"].str.contains("C", na = False)]
    return retail_refurnished

#creating revenue column
def specific():
    retail = remove()
    retail["Revenue"] = retail["Quantity"] * retail["UnitPrice"]
    revenue_per_country = retail.groupby('Country')['Revenue'].sum()
    #sampling the top 10 rated countries as per revenue
    revenue_per_country = revenue_per_country.sort_values(ascending=False).head(10)
    return revenue_per_country

#plotting a revenue graph

print(specific())
revenue_per_country = specific()
plt.figure(figsize=(7, 14))
revenue_plot_data = pd.DataFrame(revenue_per_country)
revenue_plot_graph = sns.barplot(x = 'Country', y = 'Revenue', data = revenue_plot_data)
plt.xticks(rotation=90)
plt.title("Revenue per Country (Top 10 Countries)")
plt.xlabel("Country")
plt.ylabel("Revenue")
