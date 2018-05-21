import numpy as np
import pandas as pd
import statistics as stat

file = 'instrument_data.txt'
df = pd.read_csv(file, sep='\t')

df.head(3)
# create class column
df.loc[:,'CLASS'] = df['TKPI_ASSET_TYP']

# move class column to first position
cols = df.columns.tolist()
cols = cols[-1:] + cols[:-1]
df = df[cols]

# remove column info
df = df.drop('TKPI_ASSET_TYP', 1)

# verwijder velden zonder waarde

# statistics
sf = stat.BasicStatistics(df)
#sf.to_csv('sf_out.csv', index=False)
#sf

# remove unpopulated attributes en attributes with only one unique value
# columnlist=sf.loc[(sf["unique"] > 1) & (sf["aantal"] > minimal_column_population), "column"].tolist()
#columnlist=sf.loc[(sf["unique"] > 1) & (~sf["column"].str.contains("_ID|ID_|CADIS|_NAME", na=True)), "column"].tolist()
##f_recs[f_recs['Behavior'].str.contains("nt|nv", na=False)]
##columnlist=sf.loc[(sf["unique"] > 1), "column"].tolist()
#
## create list with column names to be removed. 
#customremovelist = ['ISIN','SEDOL', 'CUSIP','SECURITY_DESCRIPTION','TKPI_SECURITY_TYP','TKPI_SUB_SECURITY_TYP', \
#                    'ASSET_TYPE','SECURITY_TYPE', 'BB_SECURITY_TYP', 'BB_SECURITY_TYP2', \
#                   'OBSOLETE', 'INACTIVE', 'mapAbility35bp',\
#                    'cHmmTssA','cHmmTssAFlnk','cHmmTxFlnk','cHmmTssBiv','cHmmBivFlnk']
#
## remove columns
#for x in customremovelist:
#    if x in columnlist: columnlist.remove(x)
#    
## make dataframe with filtered columns
#df2 = df[columnlist].reset_index()
#
#sf = stat.BasicStatistics(df2)
## todo
## remove id columns
#
