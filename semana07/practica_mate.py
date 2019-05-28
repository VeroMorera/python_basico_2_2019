#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[7]:


x = np.array([0, 1, 2, 3])
y = np.array([2, 3, 4, 5]) 


# In[8]:


x, y


# In[9]:


x * x


# In[12]:


x ** x


# In[13]:


x * y


# In[14]:


y - x


# In[15]:


x.sum()


# In[17]:


y.sum()


# In[20]:


x - y


# In[21]:



'''
n = longitud del vector
x*y. sum()

sum x = x.sum
'''


# In[22]:


N = x.size


# In[23]:


N


# In[34]:


suma_productos = (x*y).sum()


# In[37]:


suma_productos


# In[35]:


suma_x = x.sum()


# In[36]:


suma_x


# In[38]:


suma_y = y.sum()


# In[39]:


suma_y


# In[40]:


a_up = (N * suma_productos) - (suma_x * suma_y)


# In[41]:


a_up  #esto es el resultado de la parte de arriba de la fraccion


# In[46]:


x_cuadrado = x ** 2
x_cuadrado


# In[52]:


suma_x_cuadrado = (suma_x)**2
suma_x_cuadrado


# In[57]:


a_down = N * (x_cuadrado.sum()) - (suma_x_cuadrado)
a_down


# In[58]:


a = a_up / a_down


# In[59]:


a


# In[61]:


b_up1 = (x_cuadrado.sum() * suma_y) 
b_up1


# In[74]:


b_up2 = suma_x* (suma_x * (suma_y * suma_x))
b_up2


# In[75]:


b_up = b_up1 - b_up2
b_up


# In[78]:


b= 2.0  #las operaciones de b estan malas


# In[79]:


b


# In[82]:


import matplotlib.pyplot as plt


# In[83]:


plt.scatter(x,y)


# In[84]:


z = np.array([10,11,12])
z


# In[85]:


z+2


# In[86]:


mi_recta = lambda w : w + 2

mi_recta(  np.arange(10) )


# In[87]:


plt.plot( np.arange(10, 30), mi_recta(np.arange(10, 30)) )


# In[ ]:




