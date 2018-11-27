#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv(r"C:\Users\nstow\Desktop\Python\Sacramentorealestatetransactions.csv")


# In[24]:


df.plot.scatter(x='sq__ft',y='price')
plt.xlabel('Square Feet')
plt.ylabel('Price')
#This shows the price of a home verses the square footage of the home. The concentration of points at zero square feet
#is where there is no square footage data. The overall trend is that with higher square footage, the price goes higher


# In[13]:


plt.hist(df['zip'])
plt.xlabel('Zip Codes')
plt.ylabel('Number of Houses')
plt.show()

##This shows the concentration of sales by zip code. The largest bin at 95825 has over 350 sales, 
#while the smallest bin at 95500 has only around 10 sales. The 95600 bin has no sales.


# In[20]:


x1=df['beds']
x2=df['sq__ft']
y1=df['price']

plt.subplot(1,2,1)
plt.xlabel('Bedrooms')
plt.ylabel('Price')
plt.scatter(x1,y1)

plt.subplot(1,2,2)
plt.xlabel('Square Feet')
plt.ylabel('Price')
plt.scatter(x2,y1)

plt.subplots_adjust(wspace=0.5)

plt.show()
##The subplot on the left shows the relationship between price and number of bedrooms. They aren't directly related as some have
## a high number of bedrooms (3-4) but still have a low price (100K-200K) while some have a low number of bedrooms (around 2)
## but a higher price (up to around 600K).The subplot on the right shows the relationsip between square footage and price 
## with a fairly direct relationship between price and square feet, where if one goes up so does the other. Both plots have
## a nearly straight line at the zero square feet and zero bed rooms where there is no data


# In[22]:


x1=df['beds']
x2=df['baths']
y1=df['price']

plt.subplot(1,2,1)
plt.xlabel('Bedrooms')
plt.ylabel('Price')
plt.scatter(x1,y1)

plt.subplot(1,2,2)
plt.xlabel('Bathrooms')
plt.ylabel('Price')
plt.scatter(x2,y1)

plt.subplots_adjust(wspace=0.5)

plt.show()
##The subplot on the left shows the relationship between price and number of bedrooms. They aren't directly related a
## s some have a high number of bedrooms (3-4) but still have a low price (100K-200K) while some have a low number of 
## bedrooms (around 2) but a higher price (up to around 600K).The subplot on the right shows the relationsip between 
## the number of bathrooms and price with the same thing happening as with price and bedrooms. Both plots have
## a nearly straight line at the zero square feet and zero bed rooms where there is no data

