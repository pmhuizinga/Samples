# -*- coding: utf-8 -*-
"""
Created on Wed May 23 12:01:59 2018
@author: pahuizinga
"""
import pyodbc
import pandas as pd
import config
import numpy as np

def compare_master_reference(master, reference):
    master = (set(master.iloc[:, 0]))
    reference = (set(reference.iloc[:, 0]))
    # return [[x for x in master if x not in reference], [x for x in reference if x not in master]]
    return [[x for x in master if x not in reference]]

def get_data(conn_string, m_schema, m_table, m_field, r_schema, r_table, r_field):
    conn = pyodbc.connect(conn_string)
    master_sql = ("SELECT DISTINCT " + m_field + " FROM " + m_schema + "." + m_table)
    reference_sql = ("SELECT " + r_field + " FROM " + r_schema + "." + r_table)
    master_df = pd.read_sql(master_sql, conn)
    reference_df = pd.read_sql(reference_sql, conn)
    return master_df, reference_df

def main():
    conn_string = config.env_test
    master_fields = np.array(config.masterdata_master)
    reference_fields = np.array(config.masterdata_ref)
    for i in range(master_fields.shape[0]):
        master, reference = get_data(conn_string,
            master_fields[i, 1],
            master_fields[i, 2],
            master_fields[i, 3],
            reference_fields[i, 1],
            reference_fields[i, 2],
            reference_fields[i, 3]
            )
        non_matching = compare_master_reference(master, reference)
        print(master_fields[i, 1], master_fields[i, 2], master_fields[i, 3], non_matching)

if __name__ == '__main__':
    main()

