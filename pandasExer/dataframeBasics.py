import pandas as pd
df = pd.read_csv('weather_data.csv')
print(df)

df.shape # rows, columns = df.shape

df.head() # df.head(3)
df.tail() # df.tail(2)
df[1:3]
df.columns
df['day'] # or df.day
type(df['day'])
df[['day','temperature']]
df['temperature'].max()
df[df['temperature']>32]

df['day'][df['temperature'] == df['temperature'].max()] # Kinda doing SQL in pandas
df[df['temperature'] == df['temperature'].max()] # Kinda doing SQL in pandas
df['temperature'].std()
df['temperature'].mean() # But mean() won't work since data type is string

df.describe()

df.set_index('day')
df.set_index('day', inplace=True)
df
df.index
df.loc['1/2/2017']
df.reset_index(inplace=True)
df.head()

df.set_index('event',inplace=True) # this is kind of building a hash map using event as a key
df
df.loc['Snow']