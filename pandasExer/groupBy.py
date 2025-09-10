import pandas as pd
df = pd.read_csv("weather_by_cities.csv")
df

g = df.groupby("city")
g

for city, data in g:
    print("city:",city)
    print("\n")
    print("data:",data) 

g.get_group('mumbai')

g.max()

g.mean()

g.min()

g.describe()

g.size()

g.count()

g.plot()

#custom

def grouper(df, idx, col):
    if 80 <= df[col].loc[idx] <= 90:
        return '80-90'
    elif 50 <= df[col].loc[idx] <= 60:
        return '50-60'
    else:
        return 'others'

g = df.groupby(lambda x: grouper(df, x, 'temperature'))
g

for key, d in g:
    print("Group by Key: {}\n".format(key))
    print(d)