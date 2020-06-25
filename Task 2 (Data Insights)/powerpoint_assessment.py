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

# importing new data
df_cust_list = pd.read_csv('new_cust_list.csv')
df_demograph = pd.read_csv('new_cust_demo.csv')
df_address = pd.read_csv('new_cust_address.csv')
df_trans = pd.read_csv('new_transactions.csv')