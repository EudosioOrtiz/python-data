import pandas as pd
import numpy as np

df = pd.read_csv("weather_data.csv",parse_dates=['day'])
type(df.day[0])
df

df.set_index('day',inplace=True)
print(df)

new_df = df.fillna(0)
new_df

new_df = df.fillna({
        'temperature': 0,
        'windspeed': 0,
        'event': 'No Event'
    })
new_df

new_df = df.ffill()
new_df

new_df = df.bfill()
new_df

new_df = df.fillna(method="bfill", axis="columns") # axis is either "index" or "columns"
new_df

new_df = df.fillna(method="ffill",limit=1)
new_df

new_df = df.interpolate()
new_df

new_df = df.interpolate(method="time") 
new_df

new_df = df.dropna()
new_df

new_df = df.dropna(how='all')
new_df

new_df = df.dropna(thresh=1)
new_df

dt = pd.date_range("01-01-2017","01-11-2017")
idx = pd.DatetimeIndex(dt)
df.reindex(idx)

new_df = df.replace(-99999, value=np.NaN)
new_df

new_df = df.replace(to_replace=[-99999,-88888], value=0)
new_df

new_df = df.replace({
        'temperature': -99999,
        'windspeed': -99999,
        'event': '0'
    }, np.nan)
new_df

new_df = df.replace({
        -99999: np.nan,
        'no event': 'Sunny',
    })
new_df

# when windspeed is 6 mph, 7 mph etc. & temperature is 32 F, 28 F etc.
new_df = df.replace({'temperature': '[A-Za-z]', 'windspeed': '[a-z]'},'', regex=True) 
new_df

df = pd.DataFrame({
    'score': ['exceptional','average', 'good', 'poor', 'average', 'exceptional'],
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
})
df

df.replace(['poor', 'average', 'good', 'exceptional'], [1,2,3,4])