#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import json

n_dist = json.load(open("output-files/neighbor-districts-modified.json"))
d1, d2 = list(), list()
e = []
for key in n_dist:
    for val in n_dist[key]:
        if key not in e:
            e.append(key)
        if val not in e:
            d1.append(key)
            d2.append(val)
        
edge = pd.DataFrame(columns = ['i', 'j'])
for i in range(0, len(d1)):
    edge.loc[i] = [d1[i], d2[i]]
edge = edge.sort_values(by = ['i'])
edge.to_csv("output-files/edge-graph.csv", index = False)


# In[ ]:




