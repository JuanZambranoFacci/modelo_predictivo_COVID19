#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime, timedelta

import pandas as pd
import numpy as np


# In[3]:


class Datosprovinca:

    def __init__(self):
        self.download()

    def download(self):
        self.df = pd.read_csv('c:\\Users\\juank\modelo_predictivo_COVID19\\Loja\\Dataset\\Enero-Marzo_2022_Serie temporal.csv')

    def get_provincias(self, provincias, dates=True):
        co = self.df[self.df['provincia'] == provincias].iloc[:,4:].T.sum(axis = 1)
        co = pd.DataFrame(co)
        co.columns = ['Casos']
        co = co.loc[co['Casos'] > 0]

        y = np.array(co['Casos'])
        x = np.arange(y.size)
        if dates:
            start_date = pd.to_datetime(co.index[0], dayfirst=True)
            end_date = pd.to_datetime(co.index[-1], dayfirst=True)
            x_range = np.array([str(d.date()) for d in pd.date_range(start_date, end_date)])
            return np.array([x, y, x_range])
        return np.array([x, y])
    
    def show_provincias(self, start=None):
        if start:
            return self.df[self.df['provincia'].str.lower().str.contains(start.lower())]['provincia'].unique().tolist()
        else:
            return self.df['provincia'].unique().tolist()


# In[ ]:




