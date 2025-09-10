import pandas as pd
df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
})
df1

df2 = pd.DataFrame({
    "city": ["chicago","new york","orlando"],
    "humidity": [65,68,75],
})
df2

df3 = pd.merge(df1, df2, on="city")
df3

df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35, 38],
})
df1

df2 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "humidity": [65,68,71],
})
df2

df3=pd.merge(df1,df2,on="city",how="inner")
df3

df3=pd.merge(df1,df2,on="city",how="outer")
df3

df3=pd.merge(df1,df2,on="city",how="left")
df3

df3=pd.merge(df1,df2,on="city",how="right")
df3

df3=pd.merge(df1,df2,on="city",how="outer",indicator=True)
df3

df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35,38],
    "humidity": [65,68,71, 75]
})
df1

df2 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "temperature": [21,14,35],
    "humidity": [65,68,71]
})
df2

df3= pd.merge(df1,df2,on="city",how="outer", suffixes=('_first','_second'))
df3

df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
})
df1.set_index('city',inplace=True)
df1

df2 = pd.DataFrame({
    "city": ["chicago","new york","orlando"],
    "humidity": [65,68,75],
})
df2.set_index('city',inplace=True)
df2 

df1.join(df2,lsuffix='_l', rsuffix='_r')