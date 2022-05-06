#!/usr/bin/env python
# coding: utf-8

# In[2]:


from modelo_base import modeloBase

import numpy as np
from sklearn.linear_model import LinearRegression


# In[3]:


class LinearModel(modeloBase):
    plot_name = 'Linear'

    def train(self):
        x, y = np.reshape(self.x_train, (-1, 1)), np.reshape(self.y_train, (-1, 1))
        self.model = LinearRegression().fit(x, y)
        self.is_trained = True

    def predict(self):
        y_pred = self.model.predict(self.x_pred.reshape(-1, 1))
        self.y_pred = y_pred.reshape(y_pred.size)
        self.is_predicted = True


# In[ ]:




