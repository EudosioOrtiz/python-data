#Pandas Concatenate Tutorial
#Basic Concatenation
import pandas as pd

india_weather = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
    "humidity": [80, 60, 78]
})
india_weather
'''
city	humidity	temperature
0	mumbai	80	32
1	delhi	60	45
2	banglore	78	30
'''
us_weather = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
    "humidity": [68, 65, 75]
})
us_weather
'''
city	humidity	temperature
0	new york	68	21
1	chicago	65	14
2	orlando	75	35
'''
df = pd.concat([india_weather, us_weather]) # concat two data frames with his own index
df
'''
city	humidity	temperature
0	mumbai	80	32
1	delhi	60	45
2	banglore	78	30
0	new york	68	21
1	chicago	65	14
2	orlando	75	35
Ignore Index
'''
df = pd.concat([india_weather, us_weather], ignore_index=True) # concat two dataframes with single index
df
'''
city	humidity	temperature
0	mumbai	80	32
1	delhi	60	45
2	banglore	78	30
3	new york	68	21
4	chicago	65	14
5	orlando	75	35
Concatenation And Keys
'''
df = pd.concat([india_weather, us_weather], keys=["india", "us"]) # concat two dataframes indetifying his owner
df
'''
city	humidity	temperature
india	0	mumbai	80	32
1	delhi	60	45
2	banglore	78	30
us	0	new york	68	21
1	chicago	65	14
2	orlando	75	35
'''
df.loc["us"] #access to the dataframe
'''
city	humidity	temperature
0	new york	68	21
1	chicago	65	14
2	orlando	75	35
'''
df.loc["india"]
'''
city	humidity	temperature
0	mumbai	80	32
1	delhi	60	45
2	banglore	78	30
Concatenation Using Index
'''
temperature_df = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
}, index=[0,1,2])
temperature_df
'''
city	temperature
0	mumbai	32
1	delhi	45
2	banglore	30
'''
windspeed_df = pd.DataFrame({
    "city": ["delhi","mumbai"],
    "windspeed": [7,12],
}, index=[1,0])
windspeed_df
'''
city	windspeed
1	delhi	7
0	mumbai	12
'''
df = pd.concat([temperature_df,windspeed_df],axis=1) # concat two dataframes into single row with the finded values indicated in the axis using index
df
'''
city	temperature	city	windspeed
0	mumbai	32	mumbai	12.0
1	delhi	45	delhi	7.0
2	banglore	30	NaN	NaN
Concatenate dataframe with series
'''
s = pd.Series(["Humid","Dry","Rain"], name="event") # create a series named event
s
'''
0    Humid
1      Dry
2     Rain
Name: event, dtype: object
'''
df = pd.concat([temperature_df,s],axis=1) # using concat and the previous series created you can asing it with the index
df
'''
city	temperature	event
0	mumbai	32	Humid
1	delhi	45	Dry
2	banglore	30	Rain
'''

'''

axis=0 (default): Concatenates along rows (vertically). This stacks the DataFrames or Series on top of each other.
axis=1: Concatenates along columns (horizontally). This aligns the DataFrames or Series side by side.
By default, concat preserves the original indices. Use ignore_index=True to reset the index.
If the DataFrames have mismatched indices or columns, NaN will fill the missing values unless handled otherwise.

'''