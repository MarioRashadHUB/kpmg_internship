#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 07:55:05 2020

@author: MARIO P
"""


import pandas as pd

# so all columns are displayed
pd.options.display.max_columns = None
pd.options.display.max_rows = None

# importing all new recieved data
df = pd.read_csv('new_cust_list.csv')

df.columns
df.owns_car.value_counts()

# 25+ bike purchahes within past 3 years
df['25_plus'] = df['past_3_years_bike_related_purchases'].apply(lambda x: True if (x >= 25 ) else False)
df['25_plus'].value_counts()

# new df with all customers who have made more then 25 purchases
df_targetCust = df[df['25_plus'] == True]
df_targetCust['25_plus'].value_counts()

# removes all cusomers who do not own a car
df_targetCust = df_targetCust[df_targetCust['owns_car'] == 'No']
df_targetCust.owns_car.value_counts()

# removes all customers with no DOB
df_targetCust.dropna(subset = ["DOB"], inplace=True)

