#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
#from pandas import Series, DataFrame


# 
# SERIES

# In[2]:


obj = pd.Series([4, 7, -5, 3])
obj


# In[3]:


obj.values
obj.index


# In[4]:


type(obj)


# In[7]:


obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2.index


# In[8]:


obj2


# In[10]:


obj2['a'] #consultando cada index


# In[13]:


obj2[['c', 'a', 'd']] #si se ocupan varios, se debe hacer una lista


# In[14]:


obj2[obj2 < 0]


# In[15]:


obj2 * 2


# In[18]:


np.exp(obj2)


# In[19]:


'z' in obj2


# In[20]:


'b' in obj2


# In[24]:


sdata = {'Ohio': 35000, 'Texas' : 71100, 'Oregon': 1600}
obj3 = pd.Series(sdata)
obj3


# In[25]:


#mini-practica

'''
juan

notas
espanol 90
mate 80
sociales 85
ciencias 95

-crear una serie
-promedio general
-nota mayor
-nota menor
-materias >= 90

'''


# In[46]:



juanData = {'Español': 90, 'Matemáticas': 80, 'Sociales': 85, 'Ciencias': 95}

juan = pd.Series(juanData, name= 'Notas de Juan')


# In[47]:


juan


# In[35]:


lista_notas = juan.values
lista_notas


# In[51]:


promedio = lista_notas.sum() / lista_notas.size
promedio

#otra forma

juan.mean()



# In[49]:


nota_max = juan.max() 


# In[50]:


nota_max


# In[45]:


nota_min = juan.min()
nota_min


# In[53]:


juan[juan >= 90]


# In[54]:


juan[['Matemáticas', 'Ciencias']]


# In[55]:


#================================================#


# In[ ]:




