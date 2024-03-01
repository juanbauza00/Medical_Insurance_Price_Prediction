#!/usr/bin/env python
# coding: utf-8

# ## Libraries

# In[1]:


import pandas as pd


# ## Functions

# In[2]:


def calculate_outliers(column):
    q1 = column.quantile(0.25)
    q3 = column.quantile(0.75)
    iqr = q3 - q1
    
    # Define limits to identify outliers
    upper_limit = q3 + 1.5 * iqr
    lower_limit = q1 - 1.5 * iqr
    
    # Count upper and lower outliers
    upper_outliers = column[column > upper_limit].count()
    lower_outliers = column[column < lower_limit].count()
    
    # Calculate percentage of outliers
    total_values = len(column)
    upper_percentage = upper_outliers / total_values * 100
    lower_percentage = lower_outliers / total_values * 100
    
    
    
    return upper_outliers, upper_percentage, lower_outliers, lower_percentage

