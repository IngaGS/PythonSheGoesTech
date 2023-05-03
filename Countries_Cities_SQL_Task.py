#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd

data = pd.read_excel (r'C:\Users\Bendras\Downloads\Cities\PopulatinandArea.xlsx')   
df = pd.DataFrame(data)

# print(df)


# In[46]:


import pymysql
from sqlalchemy import create_engine
import mysql.connector

cnx = mysql.connector.connect(user='root',
                              password='',
                              host='localhost',
                              database='countries_cities')

engine = create_engine("mysql+pymysql://root:@localhost/countries_cities")

# Creating a cursor object
cursor = cnx.cursor()
# Create new table Cities
# query = "CREATE TABLE Cities (CityNo INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, City VARCHAR(30) NOT NULL,Country VARCHAR(30) NOT NULL,Population INT(50),Area_in_km2 VARCHAR(50));"

# cursor.execute(query)


# In[47]:


# # Import data from file to table in sql

# INSERT INTO `Cities` (`CityNo`, `City`, `Country`, `Population`, `Area_in_km2 `) VALUES (%(CityNo)s, %(City)s, %(Country)s, %(Population)s, %(Area_in_km2_)s)
# df.to_sql(name="Cities",con=engine,if_exists="append",index=False)


# In[49]:


# engine = create_engine("mysql+pymysql://root:@localhost/countries_cities")

# countries = pd.read_csv(r"C:\Users\Bendras\Downloads\Countries\europe.csv")
# countries.to_sql(name="Countries",con=engine,if_exists="append",index=False)


# In[35]:


import pandas as pd
import pymysql
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:@localhost/countries_cities")

cities = pd.read_excel(r"C:\Users\Bendras\Downloads\Cities\PopulatinandArea.xlsx")
cities.to_sql(name="cities",con=engine,if_exists="append",index=False)


# In[68]:


with engine.begin() as con:
    query = ("SELECT "+
                 " a.CityNo, a.City, a.Country, a.Population, b.Area, b.Country_ID"+
                 " FROM cities AS a JOIN countries AS b ON a.Country = b.country_name")
    cities_db = pd.read_sql(query,con)


# In[76]:


cities_db
cities_db.to_excel("Cities_IDs.xlsx")


# In[78]:


# sql = "DROP TABLE cities"
# cursor.execute(sql) 


# In[79]:


cities = pd.read_excel(r"C:\Users\Bendras\Cities_IDs.xlsx")
cities.to_sql(name="cities",con=engine,if_exists="append",index=False)


# In[80]:


cursor.execute("ALTER TABLE cities DROP CityNo")


# In[89]:


import pymysql
from sqlalchemy import create_engine
import mysql.connector

cnx = mysql.connector.connect(user='root',
                              password='',
                              host='localhost',
                              database='countries_cities')

engine = create_engine("mysql+pymysql://root:@localhost/countries_cities")

# Creating a cursor object
cursor = cnx.cursor()


cities_update = pd.read_excel(r"C:\Users\Bendras\Cities_IDs.xlsx")
#add new row to sql database from csv
cities_update.to_sql('cities', engine, index=False, if_exists='replace')


# In[86]:


# cursor.execute("ALTER TABLE cities DROP CityNo")
# cursor.execute("DELETE FROM cities WHERE City_ID = '37'")


# In[91]:


with engine.begin() as con:
    query = ("SELECT "+
                 " a.City_ID, a.City, a.Country, a.Population, b.Area, b.Country_ID, b.Capital, b.Area, b.Population"+
                 " FROM cities AS a JOIN countries AS b ON a.Country = b.country_name")
    citiescountries_db = pd.read_sql(query,con)
    
# citiescountries_db
# citiescountries_db.to_excel("Cities_Countries.xlsx")
citiescountries_db.to_csv("Cities_Countries.csv")


# In[ ]:




