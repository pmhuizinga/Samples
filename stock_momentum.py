# Libraries
import pandas as pd
import numpy as np

# Variables
nr_of_stocks = 2 # Number of best performing stocks
nr_of_cumulative_periods = 4 # Number of periods to calculate cumulative returns
rebalance_frequency = 2 # Number of periods to rebalancing
transaction_costs = 0.01 # 1%

def open_file(filename, sheetname):
    df = pd.read_excel(filename, sheetname, header=0)
    return df

def data_prep(df):
    # Verwijder eerste record (met datastream security code)
    df = df[1:]
    # even tijdelijk het bereik verkleinen tbv test
    # df = df.iloc[0:20,0:10]
    # Sortering op datum
    df.sort_values(by=['Name'])
    return df

def calc_basket_return(df, nr_of_stocks, nr_of_cumulative_periods, rebalance_frequency, transaction_costs):
    # Maak arrays aan voor cumulatieve rendementen en voor gewichten
    df_internal = df.copy(deep=True)
    df_cum = df.copy(deep=True) # array voor cumulatieve 
    df_contribution = df.copy(deep=True)
    
    # replace market values in df with monthly returns and append cumulative returns to df_cum dataframe.
    for x in df.columns.tolist()[1:]:
        #df_weight[x] = df[x].cumsum(df).fillna(0)
        df_internal[x] = df_internal[x].pct_change().fillna(0) # monthly returns
        df_cum[x] = df_cum[x].pct_change(periods=nr_of_cumulative_periods).fillna(0) # cumulative returns
    
    # sort descending on cumulative returns replace top 'nr_of_stocks' with avg weight and the remainder with zeros.
    weights = np.where(np.argsort(-df_cum.iloc[:,1:]) >= nr_of_stocks, 0, 1/nr_of_stocks)  # het minteken bepaald de sorteringsvolgorde
    #weights_rebal = np.where(np.mod(weights[:]-nr_of_cumulative_periods, rebalance_frequency),'a','b') # kan het in 1 keer?
    weights_rebal =  np.empty(shape=[weights.shape[0],weights.shape[1]])
    
    # bepaal gewicht rekening houdend met de rebalance frequency
    for x in range(weights.shape[0]): # rows
        for y in range(weights.shape[1]): # columns
            weights_rebal[x][y] = weights[x-np.mod(x-nr_of_cumulative_periods,rebalance_frequency)][y]
    
    # bepaal de contributie (weights_rebal * maand rendement)
    for x in range(df_internal.shape[0]):
        for y in range(df_internal.shape[1])[1:]:
            df_contribution.iloc[x,y] = df_internal.iloc[x,y] * weights_rebal[x][y-1]
    
    # Bepaal cumulatief rendement van de basket. de eerste maanden (nr_of_cumulative_periods) worden niet meegenomen)
    result = (np.cumprod((1+(df_contribution.iloc[nr_of_cumulative_periods:,1:].sum(axis=1))))-1).iloc[-1] 
    return result

df = open_file('AEX-data.xlsx', 'total returns aandelen')
df = data_prep(df)

calculated_return = calc_basket_return(df, 2, 4, 2, 0.01)

# test
for i in range(2, 5):
    for j in range(1, 5):
        for x in range(1, 5):
            print("stocks:", i, "period:", j, "rebalance:", x, "return:", calc_basket_return(df, i, j, x, 0.01))
            


    


