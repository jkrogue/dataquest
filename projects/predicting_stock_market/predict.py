import pandas as pd
from datetime import datetime

data = pd.read_csv('sphist.csv')
data['Date'] = pd.to_datetime(data['Date'], yearfirst=True)
data = data.sort_values(by='Date',ascending=True)
print(data.head())

data['avg_5_day'] = -1
data['ratio_5_365'] = -1
data['std_5_day'] = -1
start_index = data[data['Date'] > datetime(year=1951, month=1, day=2)].index[0]

index = 0
index_5_days = index + 5
index_365_days = index + 365
print(data.index.get_loc(data.iloc[0].name))
avg_5_day = data.loc[index+1:index_5_days]['Close'].mean()
ratio_5_365 = avg_5_day / data.loc[index+1:index_365_days]['Close'].mean()
std_5_day = data.loc[index+1:index_5_days]['Close'].std()

exit()
def calc_metrics(row):
    idx = row.name
    index_5_days = index + 5
    index_365_days = index + 365
    row['avg_5_day'] = data.loc[index+1:index_5_days]['Close'].mean()
    row['ratio_5_365'] = row['avg_5_day'] / data.loc[index+1:index_365_days]['Close'].mean()
    row['std_5_day'] = data.loc[index+1:index_5_days]['Close'].std()
    
    
    return row
    
data = data.apply(calc_metrics, axis=1)
print(data.tail())