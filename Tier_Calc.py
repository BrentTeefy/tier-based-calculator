
# coding: utf-8

# In[104]:




# In[105]:

import operator as op
import functools as ft


# In[106]:


def tier_calc(volume,rateid,dic):
    l1 = []
    l2 = []
    l3 = []
    tiers = dic[rateid]['tiers']
    rates = dic[rateid]['rates']
    m=0
    for x in tiers:
        l1.append(volume-x)
    for y in l1:
        l2.append(1 if y>0 else 0)
    for z in rates:
        l3.append(z-m)
        m=z
    return sum(ft.reduce(op.mul, data) for data in zip(l1,l2,l3))   
        


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



