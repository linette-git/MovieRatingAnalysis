#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


movies=pd.read_csv("movies.csv",delimiter='::',header=None,engine='python')


# In[3]:


movies.head()


# In[4]:


ratings=pd.read_csv("ratings.csv",delimiter='::',header=None,engine='python')


# In[5]:


ratings.head()


# In[6]:


movies.columns=['ID','TITLE','GENRE']


# In[7]:


ratings.columns=['USER','ID','RATINGS','TIMESTAMP']


# In[8]:


movies.head()


# In[9]:


ratings.head()


# In[10]:


data=pd.merge(movies,ratings,on=["ID","ID"])


# In[11]:


data.head()


# In[12]:


data.shape


# In[13]:


data.info()


# In[14]:


data.describe()


# In[15]:


ratings=data['RATINGS'].value_counts()
numbers = ratings.index
fig1, ax1 = plt.subplots(figsize=(15, 10))
plt.pie(ratings,autopct='%1.1f%%')
plt.title('Distibution of ratings')
plt.legend(title = "RATINGS:",loc='upper right',labels=numbers)
plt.show()


# In[16]:


data2 = data.query("RATINGS == 10")


# In[17]:


#top 10 movies with 10 ratings
data2['TITLE'].value_counts().head(10)


# In[18]:


#Here Joker (2019) got the highest number of 10 ratings from viewers

