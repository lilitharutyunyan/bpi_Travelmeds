#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import re
import pandas as pd

# In[3]:


def split_strength(string):
    if type(string) == type(7.5):
        return np.nan, np.nan
    elif string in ('nan','[]',''):
        return np.nan, np.nan
    elif string is None:
        return np.nan, np.nan
    elif string.isnumeric():
        return string, np.nan

    else:
        try:
            value = re.findall(r'[\d.]+', string)[0]
            unit = re.findall(r'[\s]?(?:mg \/ ml| mg \/ l| mg|mg| g \/ ml| g \/ l| g|g| µg \/ ml| µg \/ l| µg|µg| mcg \/ ml| mcg \/ l| mcg|mcg| ml|ml| l|l)',string)[0]
            return value, unit
        except:
            return np.nan, np.nan


# In[4]:


def reorder_dfs(df):
    df_new = pd.DataFrame()
    df_new['product'] = df['product'].str.upper()
    df_new['country'] = df['country'].str.upper()
    df_new['drug'] = df['drug'].str.upper()
    df_new['route'] = df['route'].str.upper()
    df_new['strength'] = df['strength']
    df_new['unit'] = df['unit']
    return df_new


# In[ ]:




