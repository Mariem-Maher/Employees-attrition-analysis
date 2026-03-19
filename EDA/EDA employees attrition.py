#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


# In[2]:


data=pd.read_csv('cleaned data.csv')
df=pd.DataFrame(data)


# Dataset overview
# 

# In[3]:


df.describe()


# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


df['Attrition'].value_counts()


# In[7]:


df['Attrition'].value_counts()*100/len(df)


# In[8]:


print(df['BusinessTravel'].value_counts())


# In[9]:


print(df['Department'].value_counts())


# In[10]:


print(df['JobRole'].value_counts())


# In[11]:


print(df['Gender'].value_counts())


# Exploring attrition factors

# In[12]:


df.groupby('Attrition')['MonthlyIncome'].mean()


# In[13]:


stayed=df[df['Attrition']==0]['MonthlyIncome']
left=df[df['Attrition']==1]['MonthlyIncome']
t_stat,p_value=stats.ttest_ind(stayed,left)
print(t_stat,p_value)


# In[14]:


df.groupby(['Attrition','BusinessTravel']).size()


# In[15]:


df.groupby(['Attrition','Department']).size()


# In[ ]:





# In[16]:


df.groupby(['Attrition','JobRole']).size()


# In[17]:


df.groupby(['Attrition','OverTime']).size()


# In[18]:


stayed=df[df['Attrition']==0]['OverTime']
left=df[df['Attrition']==1]['OverTime']
t_stat,p_value=stats.ttest_ind(stayed,left)
print(t_stat,p_value)


# In[19]:


df.groupby(['Attrition','JobSatisfaction']).size()


# In[20]:


stayed=df[df['Attrition']==0]['JobSatisfaction']
left=df[df['Attrition']==1]['JobSatisfaction']
t_stat,p_value=stats.ttest_ind(stayed,left)
print(t_stat,p_value)


# In[ ]:





# In[21]:


df.groupby(['Attrition','Gender']).size()


# In[22]:


df.groupby(['Attrition','MaritalStatus']).size()


# In[23]:


df.groupby(['Attrition','Salary_hike_Group']).size()


#  Demographic Analysis
# 

# In[24]:


df['Age Group'].value_counts().plot(kind='bar')
plt.xlabel('Age Group')
plt.ylabel('Number of employees')
plt.title('Distribution of Age groups')
plt.show()


# In[25]:


df['Distance Group'].value_counts().plot(kind='pie')
plt.xlabel('Distance Group')
plt.ylabel('Number of employees')
plt.title('Distribution of Distance Groups')
plt.show()


# In[26]:


df['EducationField'].value_counts().plot(kind='bar')
plt.xlabel('EducationField')
plt.ylabel('Number of employees')
plt.title('Distribution of Education Field')
plt.show()


# In[27]:


df['MaritalStatus'].value_counts().plot(kind='pie')
plt.xlabel('MaritalStatus')
plt.ylabel('Number of employees')
plt.title('Distribution of Marital Status')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




