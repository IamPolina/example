#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[23]:


import numpy as np
import sys
import hump
import matplotlib.pyplot as plt

def disappointing_fun(maximum):

    xx = np.full(maximum-1, 0.)
    yy = np.full(maximum-1, 0.)
    y0 = 0.5
    beta = 3.
    for n in range(1,maximum):
        hArray = hump.series(n, y0, beta)
        xx[n-1] = len(hArray)
        yy[n-1] = sys.getsizeof(hArray)
    print(xx,yy)
    plt.plot(xx,yy)
    plt.scatter(xx,yy,c='r')
    plt.xlabel('length of array')
    plt.ylabel('memory used')
    plt.show()
        


# In[25]:


disappointing_fun(100)


# In[ ]:





# In[ ]:


n


# In[ ]:




