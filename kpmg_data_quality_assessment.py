# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:01:18 2020

@author: Mario
"""

import pandas as pd

#so all columns are displayed
pd.options.display.max_columns = None
pd.options.display.max_rows = None

# imports all three datasets
df_demograph = pd.read_csv('customer_demgraph.csv')
df_address = pd.read_csv('customer_addresses.csv')
df_trans = pd.read_csv('customer_transactions.csv')

# drops all duplicate values
df_demograph.drop_duplicates(keep=False, inplace=True)
df_address.drop_duplicates(keep=False, inplace=True)
df_trans.drop_duplicates(keep=False, inplace=True)

df_demograph.columns
df_address.columns
df_trans.columns

df_demograph.head()
df_address.head()
df_trans.head()

df_demograph.info()
df_address.info()
df_trans.info()

df_demograph.isnull().any()
df_address.isnull().any()
df_trans.isnull().any()

df_demograph.isnull().sum()
df_address.isnull().sum()
df_trans.isnull().sum()

df_demograph.isnull().sum() / df_demograph.shape[0]
df_trans.isnull().sum() / df_trans.shape[0]


df_address.customer_id.value_counts()
df_address.address.value_counts()
df_address.postcode.value_counts()
df_address.state.value_counts()
df_address.country.value_counts()

df_demograph.customer_id.value_counts()
df_demograph.gender.value_counts()
df_demograph.job_title.value_counts()

df_trans.order_status.value_counts()
