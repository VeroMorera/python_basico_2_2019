#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[4]:


my_list = [-17, 0, 4, 5, 9]
my_array_from_list = np.array(my_list)
my_array_from_list


# In[5]:


my_array_from_list * 10


# In[6]:


my_array_from_list + 1


# In[ ]:


#SLICING ARRAY


# In[15]:


my_vector = np.array([-17, -4, 0, 2, 21, 37, 105])


# In[16]:


my_vector[0]


# In[19]:


my_vector[0] = 3333


# In[24]:


my_vector


# In[23]:


my_vector.size


# In[25]:


#matrix

my_array = np.arange(35) #cantidad de elementos en la matriz
my_array.shape = (7,5)  #si queremos que sea matriz de 7x5
my_array


# In[26]:


my_array[2]


# In[27]:


my_array[2][0]


# In[28]:


my_array[-2]


# In[29]:


my_array[5,2]


# In[31]:


np.arange(10, 23)


# In[32]:


np.arange(10, 23) -10  #le resta 10 a todos 


# In[33]:


np.arange(10, 23).size


# In[34]:


#para hacer saltos, en este caso de cada 5
np.arange(10, 23, 5)


# In[36]:


#otra forma
np.arange(26, step=5)


# In[ ]:




