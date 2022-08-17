#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd

data = pd.read_csv(r'C:\Users\SATGOSWAMI\Documents\Composite Anlytics\nullhypothesis.csv')
print(data)
data.head()


# In[9]:


data['diff'] = data['Observed'] - data['Expected']
data['diff^2'] = data['diff'] ** 2
data.head()


# In[10]:


len(data)


# In[16]:


numerator = (data['diff^2'])
denominator = data['Expected']
chi_sq = sum(numerator/denominator)
print (chi_sq)


# In[ ]:


### degree of freedom is 1, 
### tabulated value of chi_sq for 1 D.f at 5% significance level is 3.84. 
### So, calculated chi_sq < tabulated chi_sq. 
### We reject null hypothesis 


# In[23]:


import pandas as pd

data1 = pd.read_csv(r'C:\Users\SATGOSWAMI\Documents\Composite Anlytics\alternatehypothesis.csv')
print(data1)
data1.head()


# In[24]:


data1['diff'] = data1['Observed'] - data1['Expected']
data1['diff^2'] = data1['diff'] ** 2
data1.head()


# In[21]:


len(data1)


# In[25]:


numerator = (data1['diff^2'])
denominator = data1['Expected']
chi_sq = sum(numerator/denominator)
print (chi_sq)


# In[ ]:


### degree of freedom is 1, 
### tabulated value of chi_sq for 1 D.f at 5% significance level is 3.84. 
### So, calculated chi_sq > tabulated chi_sq. 
### We reject alternate hypothesis 

