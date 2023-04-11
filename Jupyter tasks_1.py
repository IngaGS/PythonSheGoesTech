#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas


# In[5]:


data=pandas.read_excel('https://stats.vmi.lt/lt/statistics/pvm-deklaraciju-duomenys-menesiais/?export=xlsx', index_col=0, header=8)
data


# In[7]:


data1 = data.reset_index()
data1


# In[8]:


data2 = data1.drop_duplicates().dropna()
data2


# In[9]:


import statistics


# In[10]:


PurchasesLT=data2['Pirkimai Lietuvoje']
statistics.mean(PurchasesLT)


# In[11]:


statistics.median(PurchasesLT)


# In[12]:


statistics.stdev(PurchasesLT)


# In[13]:


import matplotlib.pyplot as pl


# In[15]:


period=data2['Laikotarpis']


# In[17]:


pl.scatter(PurchasesLT, period)


# In[20]:


shares=pandas.read_excel('https://nasdaqbaltic.com/statistics/en/shares?download=1')
shares


# In[22]:


group=shares.groupby(['MarketPlace'])
group.size()


# In[23]:


group_list=shares.groupby(['List/segment'])
group_list.size()


# In[25]:


group_industry=shares.groupby(['Industry'])
group_industry.size()


# In[32]:


pl.title("Purchases in Lithuania, 2022-2023 mln Eur")
pl.xlabel('Period')
pl.ylabel('Purchases in Lithuania, mln Eur')
pl.tick_params(axis='x', labelrotation=90)
data_subset = data2.iloc[:14, :]

pl.plot(data_subset['Laikotarpis'], data_subset['Pirkimai Lietuvoje'])


# In[40]:


merge1=pandas.read_excel('C:\\Users\\Bendras\\Downloads\\shares1.xlsx')
merge2=pandas.read_excel('C:\\Users\\Bendras\\Downloads\\shares2.xlsx')



merged_data = pandas.merge(merge1, merge2, on='Ticker', how='inner')
merged_data


# In[44]:


SalesLT = data2['Pardavimai Lietuvoje']
PurchasesLT = data2['Pirkimai Lietuvoje']
SalesAll = data2['Pardavimai iš viso']

datagraph = [SalesLT, PurchasesLT, SalesAll]

pl.ylabel("Mln eur")

pl.boxplot(datagraph)


# In[45]:


Avg_price=shares['Average Price']

pl.title("Average share price on 2023-04-11")

pl.hist(Avg_price)


# In[ ]:




