import requests
import numpy as np 
import pandas as pd 
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"
page=requests.get(url).text
# print(page)

#beautifulsoup implementation
soup=BeautifulSoup(page,'lxml')
# print(soup)

getTable=soup.find("table",id="main_table_countries_today")
# print(getTable)

getTableData = getTable.tbody.find_all("tr", attrs={'class': None, 'style:': None})

# print(getTableData) 

dic={}
for i in range(len(getTableData)):
    
    if getTableData[i].find_all("a", href=True):
        key=getTableData[i].find_all("a", href=True)[0].string
        # key=getTableData[i].find_all("td")[0].string
        # print(key)

    values=[j.string for j in getTableData[i].find_all('td')]
    dic[key]=values

# print(dic)
column_names = ["Total Cases", "New Cases","Total Deaths", "New Deaths","Total Recovered", "Active Cases","Serious,Critical ", "Tot Cases/1M pop","Deaths/1M pop", "Total Tests", "Tests/1M pop", "Population"]
df=pd.DataFrame(dic).iloc[1:,:].T.iloc[:,:12]
df.index_name="country"
df.columns=column_names
print(df)
# df.to_csv("COVID.csv")