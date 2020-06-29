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

