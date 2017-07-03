# coding: utf-8

# Create financial dataset of 3 big technologies using `quandl` package
# 
# Useful links
# 
# * Search QUANDL CODE: https://www.quandl.com/search?query=facebook

# In[4]:
import os

import quandl
import pandas as pd


def load_stock_datasets():
    data_file = "stocks.xlsx"
    if os.path.isfile(data_file):
        stocks = pd.read_excel(data_file)
    else:
        quandl.ApiConfig.api_key = 'a5JKbmNDb4k98huTPMcY'
        google = quandl.get('WIKI/GOOGL')
        google["Company"] = "Google"
        facebook = quandl.get('WIKI/FB')
        facebook["Company"] = "Facebook"
        apple = quandl.get('WIKI/AAPL')
        apple["Company"] = "Apple"
        stocks = pd.concat([apple, facebook, google])
        stocks = stocks.reset_index()
        stocks.to_excel(data_file, index=False)
    return stocks


import seaborn as sns

# In[9]:
import matplotlib.pyplot as plt
ax = plt.subplot()
stocks = load_stock_datasets()
stocks = stocks.head(1000)
# ax = sns.tsplot(stocks, time="Date", value="Close", unit="Company")
ax = sns.pointplot(x="Date", y="Close", hue="Company", data=stocks)
plt.show()


print(0)


# In[ ]:
