#Pandas Merge Tutorial
#Basic Merge Using a Dataframe Column
import pandas as pd
df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
})
df1
'''
city	temperature
0	new york	21
1	chicago	14
2	orlando	35
'''
df2 = pd.DataFrame({
    "city": ["chicago","new york","orlando"],
    "humidity": [65,68,75],
})
df2
'''
city	humidity
0	chicago	65
1	new york	68
2	orlando	75
'''
df3 = pd.merge(df1, df2, on="city")
df3
'''
city	temperature	humidity
0	new york	21	68
1	chicago	14	65
2	orlando	35	75
Type Of DataBase Joins
<img src="db_joins.jpg" height="800", width="800">
'''
df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35, 38],
})
df1
'''
city	temperature
0	new york	21
1	chicago	14
2	orlando	35
3	baltimore	38
'''
df2 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "humidity": [65,68,71],
})
df2
'''
city	humidity
0	chicago	65
1	new york	68
2	san diego	71
'''
df3=pd.merge(df1,df2,on="city",how="inner")
df3
'''
city	temperature	humidity
0	new york	21	68
1	chicago	14	65
'''
df3=pd.merge(df1,df2,on="city",how="outer")
df3
'''
city	temperature	humidity
0	new york	21.0	68.0
1	chicago	14.0	65.0
2	orlando	35.0	NaN
3	baltimore	38.0	NaN
4	san diego	NaN	71.0
'''
df3=pd.merge(df1,df2,on="city",how="left")
df3
'''
city	temperature	humidity
0	new york	21	68.0
1	chicago	14	65.0
2	orlando	35	NaN
3	baltimore	38	NaN'''
df3=pd.merge(df1,df2,on="city",how="right")
df3
'''
city	temperature	humidity
0	new york	21.0	68
1	chicago	14.0	65
2	san diego	NaN	71
indicator flag
'''
df3=pd.merge(df1,df2,on="city",how="outer",indicator=True)
df3
'''
city	temperature	humidity	_merge
0	new york	21.0	68.0	both
1	chicago	14.0	65.0	both
2	orlando	35.0	NaN	left_only
3	baltimore	38.0	NaN	left_only
4	san diego	NaN	71.0	right_only
suffixes
'''
df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35,38],
    "humidity": [65,68,71, 75]
})
df1
'''
city	humidity	temperature
0	new york	65	21
1	chicago	68	14
2	orlando	71	35
3	baltimore	75	38
'''
df2 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "temperature": [21,14,35],
    "humidity": [65,68,71]
})
df2
'''
city	humidity	temperature
0	chicago	65	21
1	new york	68	14
2	san diego	71	35
'''
df3= pd.merge(df1,df2,on="city",how="outer", suffixes=('_first','_second'))
df3
'''
city	humidity_first	temperature_first	humidity_second	temperature_second
0	new york	65.0	21.0	68.0	14.0
1	chicago	68.0	14.0	65.0	21.0
2	orlando	71.0	35.0	NaN	NaN
3	baltimore	75.0	38.0	NaN	NaN
4	san diego	NaN	NaN	71.0	35.0
join
'''
df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
})
df1.set_index('city',inplace=True)
df1
'''
temperature
city	
new york	21
chicago	14
orlando	35
'''
df2 = pd.DataFrame({
    "city": ["chicago","new york","orlando"],
    "humidity": [65,68,75],
})
df2.set_index('city',inplace=True)
df2
'''
humidity
city	
chicago	65
new york	68
orlando	75
'''
df1.join(df2,lsuffix='_l', rsuffix='_r')
'''
temperature	humidity
city		
new york	21	68
chicago	14	65
orlando	35	75
'''