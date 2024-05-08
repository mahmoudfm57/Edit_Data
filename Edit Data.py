#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv(r'C:/Users/MahmoudMohamedHel202/Desktop/ملفات عمل/Orders.csv',skiprows=4)
df


# In[3]:


df.dropna(how='all',inplace=True)


# In[4]:


df


# In[5]:


df['City']=df['City'].str.title()


# In[6]:


df


# In[7]:


df['Branch']=df['Branch'].str.upper()
df['Email']=df['Email'].str.lower()


# In[8]:


df


# In[9]:


df['Phone Number']= df['Phone Number'].str.replace('Tel: ','')
df


# In[10]:


df['Discount']=df['Discount'].round(0)
df


# In[11]:


df['Total Price']=df['Quantity'] * df['Unit Price']


# In[12]:


df


# In[13]:


df['Cost']=df['Total Price'] - df['Discount'].fillna(0)
df


# In[14]:


df['Customer Full Name']=df['Customer Full Name'].str.title()


# In[ ]:


newcolumn=df['Branch'].str[:2]
df.insert(5,'BrCode',newcolumn)
df


# In[ ]:


df


# In[ ]:


df.loc[df['Status']== True,'Order Status']='Done'
df.loc[df['Status']== False,'Order Status']='Pending'
df.loc[(df['Status']== False)&(df['Order Date'] <='2020/01/01') ,'Order Status']='Canceled'
df


# In[ ]:


def level(row):
    if row > 1000:
        return 'High'
    else :
        return 'Low'
df['Cost Level']=df['Cost'].apply(level)
df


# In[ ]:


import numpy as np


# In[ ]:


df['Discount Description']= np.where(df['Discount'].isnull(),'No Discount',df['Discount']/df['Cost'])
df


# In[ ]:





# In[ ]:


df.to_excel(r'C:\Users\MahmoudMohamedHel202\Desktop\ملفات عمل\MyNweOrders.xlsx')


# In[ ]:




