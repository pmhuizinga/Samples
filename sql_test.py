# -*- coding: utf-8 -*-
"""
Created on Wed May 23 12:01:59 2018
@author: pahuizinga
"""
import pyodbc
import pandas as pd
import statistics as stat

conn = pyodbc.connect(
    r'DRIVER={SQL Server};'
    r'SERVER=UKDBCSDEVCLD001\CLD01DEV;'
    r'DATABASE=Markit_EDM_TEST_v95;'
    r'Trusted_Connection=yes;'
    )

sql = "SELECT * FROM T_MASTER_SEC"

df = pd.read_sql(sql, conn)

sf = stat.BasicStats(df)





