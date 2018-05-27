# -*- coding: utf-8 -*-
"""
Created on Wed May 23 12:01:59 2018
@author: pahuizinga
"""
import pyodbc
import pandas as pd
import config
import statistics as stat

# def get_dq_data(conn_string, table):
#     for i in range(len(master_tables)):
#         statistics = get_table_data(conn_string, master_tables[i])
#         information_schema = get_sql_information_schema_data(conn_string, master_tables[i])
#         merged_frame = merge_frames(statistics, information_schema)
#         print(merged_frame)
#         totalframe = pd.concat(totalframe, merged_frame)

def get_table_data(conn_string, table):
    conn = pyodbc.connect(conn_string)
    sql = ("SELECT * FROM " + table)
    df = pd.read_sql(sql, conn)
    sf = stat.BasicStats(df)
    return sf

def get_sql_information_schema_data(conn_string, table):
    conn = pyodbc.connect(conn_string)
    sql = ("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '" + table.split('.')[1] + "'")
    df = pd.read_sql(sql, conn)
    return df

def merge_frames(frame1, frame2):
    total = frame1.merge(frame2, left_on='column', right_on='COLUMN_NAME', how='outer')
    return total

def main():
    totalframe=[]
    conn_string = config.env_test
    master_tables = config.master_tables.split(',')

    for i in range(len(master_tables)):
        statistics = get_table_data(conn_string, master_tables[i])
        information_schema = get_sql_information_schema_data(conn_string, master_tables[i])
        merged_frame = merge_frames(statistics, information_schema)
        print(merged_frame)
    #     totalframe = pd.concat(totalframe, merged_frame)
    # print(totalframe)

if __name__ == '__main__':
        main()



